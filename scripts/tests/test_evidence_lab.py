"""Sentetik fikstürlerle test. Sentetik veri asla gerçek kullanıcı kanıtı değildir."""
import csv
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from evidence_core import (EvidenceError, analyze_pair, compare_videos, extract_frames,
                           parse_timestamps, summarize_study)
from evidence_lab import check_case
from evidence_suite import run_suite
from prototype_capture import validate_config, is_local_url

try:
    from PIL import Image
except ImportError:
    Image = None


class TestVisualEvidence(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    @unittest.skipIf(Image is None, "Pillow not installed")
    def test_identical_screens_have_zero_difference(self):
        ref, candidate = self.root / "ref.png", self.root / "candidate.png"
        Image.new("RGB", (80, 80), (20, 40, 60)).save(ref)
        shutil.copy(ref, candidate)
        result = analyze_pair(ref, candidate, self.root / "diff")
        self.assertEqual(result["metrics"]["rgb_mean_absolute_error_0_to_1"], 0)
        self.assertEqual(result["metrics"]["changed_pixel_fraction_0_to_1"], 0)
        self.assertTrue((self.root / "diff" / "overlay.png").exists())

    @unittest.skipIf(Image is None, "Pillow not installed")
    def test_changed_screen_has_detectable_difference(self):
        ref, candidate = self.root / "ref.png", self.root / "candidate.png"
        Image.new("RGB", (80, 80), (0, 0, 0)).save(ref)
        Image.new("RGB", (80, 80), (255, 255, 255)).save(candidate)
        result = analyze_pair(ref, candidate, self.root / "diff")
        self.assertEqual(result["metrics"]["rgb_mean_absolute_error_0_to_1"], 1)
        self.assertEqual(result["metrics"]["changed_pixel_fraction_0_to_1"], 1)

    @unittest.skipIf(Image is None, "Pillow not installed")
    def test_dimension_mismatch_is_not_silently_resized(self):
        ref, candidate = self.root / "ref.png", self.root / "candidate.png"
        Image.new("RGB", (40, 50)).save(ref)
        Image.new("RGB", (40, 51)).save(candidate)
        with self.assertRaisesRegex(EvidenceError, "viewport"):
            analyze_pair(ref, candidate, self.root / "diff")

    def test_timestamp_guard(self):
        self.assertEqual(parse_timestamps("0,0.5,1.2"), [0, .5, 1.2])
        for raw in ["1,0", "-1", "1,1", "NaN", "", "10,hey"]:
            with self.subTest(raw=raw), self.assertRaises(EvidenceError):
                parse_timestamps(raw)

    @unittest.skipUnless(shutil.which("ffmpeg") and shutil.which("ffprobe") and Image, "FFmpeg/Pillow not installed")
    def test_video_frame_extraction_and_comparison(self):
        a, b = self.root / "a.mp4", self.root / "b.mp4"
        for path, color in [(a, "blue"), (b, "red")]:
            subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "lavfi", "-i",
                            f"color=c={color}:s=64x64:d=1:r=5", "-c:v", "mpeg4", str(path)],
                           check=True, capture_output=True)
        got = extract_frames(a, [0.0, .2], self.root / "frames")
        self.assertEqual(len(got["frames"]), 2)
        compared = compare_videos(a, b, [0.0, .2], self.root / "video_diff")
        self.assertGreater(compared["mean_frame_rgb_error"], .1)


class TestHumanEvidence(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def write_csv(self, rows):
        path = self.root / "study.csv"
        with path.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["participant_id", "variant", "consent", "task_complete", "task_seconds", "noticed", "understood", "surprise_1_5", "liking_1_5", "recall_24h", "negative_effect"])
            w.writeheader()
            w.writerows(rows)
        return path

    def row(self, ident="p1", variant="A", consent="yes", **kw):
        x = {"participant_id": ident, "variant": variant, "consent": consent, "task_complete": "yes",
             "task_seconds": "30", "noticed": "yes", "understood": "yes", "surprise_1_5": "4",
             "liking_1_5": "3", "recall_24h": "", "negative_effect": "no"}
        return {**x, **kw}

    def test_empty_csv_is_not_fabricated(self):
        with self.assertRaisesRegex(EvidenceError, "Gerçek kullanıcı verisi yok"):
            summarize_study(self.write_csv([]), self.root / "out.json")

    def test_consent_filter_and_evidence_level(self):
        report = summarize_study(self.write_csv([
            self.row("p1", "A"), self.row("p2", "A", consent="no"),
            self.row("p3", "B", noticed="no", liking_1_5="1")]), self.root / "out.json")
        self.assertEqual(report["consent_excluded"], 1)
        self.assertEqual(report["evidence_level"], "E2_observed_pilot")
        self.assertEqual(report["groups"]["A"]["participants"], 1)
        self.assertEqual(report["groups"]["B"]["noticed_rate"], 0)
        self.assertIsNone(report["groups"]["A"]["recall_24h_rate"])
        self.assertNotIn("p1", json.dumps(report))

    def test_invalid_rating_and_duplicate_participant(self):
        with self.assertRaises(EvidenceError):
            summarize_study(self.write_csv([self.row(liking_1_5="6")]), self.root / "out.json")
        with self.assertRaises(EvidenceError):
            summarize_study(self.write_csv([self.row(), self.row()]), self.root / "out.json")

    def test_gate_blocks_negative_effect_with_real_study_report(self):
        rows = [self.row(f"p{i}", "A", negative_effect="yes" if i == 1 else "no") for i in range(8)]
        summarize_study(self.write_csv(rows), self.root / "study.json")
        case = {"case_id": "p-01", "reference_id": "ref-1", "hypothesis": "daha sakin",
                "technical_evidence": [], "human_evidence": {"report": "study.json"},
                "acceptance": {"min_human_per_variant": 8, "max_negative_effect_count": 0}}
        path = self.root / "case.json"
        path.write_text(json.dumps(case), encoding="utf-8")
        result = check_case(path, self.root / "gate.json")
        self.assertEqual(result["status"], "failed")
        self.assertIn("olumsuz etki", result["failed"][0])

    def test_gate_never_claims_human_validation_without_users(self):
        case = {"case_id": "p-01", "reference_id": "ref-1", "hypothesis": "kedi dikkati çeker",
                "technical_evidence": [], "human_evidence": None, "acceptance": {"min_human_per_variant": 8}}
        path = self.root / "case.json"
        path.write_text(json.dumps(case), encoding="utf-8")
        result = check_case(path, self.root / "gate.json")
        self.assertEqual(result["status"], "limited_or_blocked")
        self.assertFalse(result["visual_quality_is_human_validated"])
        self.assertEqual(len(result["used_reports"]), 0)

    @unittest.skipIf(Image is None, "Pillow not installed")
    def test_gate_can_fail_measured_visual_threshold(self):
        ref = self.root / "ref.png"
        cand = self.root / "cand.png"
        Image.new("RGB", (30, 30), "black").save(ref)
        Image.new("RGB", (30, 30), "white").save(cand)
        analyze_pair(ref, cand, self.root / "diff")
        case = {"case_id": "p-01", "reference_id": "ref-1", "hypothesis": "görsel korunacak",
                "technical_evidence": [{"report": "diff/report.json"}], "human_evidence": None,
                "acceptance": {"max_rgb_mae": .1}}
        path = self.root / "case.json"
        path.write_text(json.dumps(case), encoding="utf-8")
        result = check_case(path, self.root / "gate.json")
        self.assertEqual(result["status"], "failed")
        self.assertTrue(result["failed"])


class TestContinuousEvidenceSuite(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def write_config(self, cases):
        path = self.root / "suite.json"
        path.write_text(json.dumps({"project": "test", "cases": cases}), encoding="utf-8")
        return path

    def test_zero_cases_is_not_success(self):
        with self.assertRaisesRegex(EvidenceError, "boş test başarı değildir"):
            run_suite(self.write_config([]), self.root / "out")

    def test_missing_image_fails_closed(self):
        cfg = self.write_config([{"id": "home", "kind": "image", "target_state": "home-390",
                                  "reference": "no.png", "candidate": "no2.png", "max_rgb_mae": 0.1}])
        report = run_suite(cfg, self.root / "out")
        self.assertEqual(report["status"], "blocked")
        self.assertEqual(report["results"][0]["status"], "blocked")

    @unittest.skipIf(Image is None, "Pillow not installed")
    def test_real_images_pass_and_fail_by_threshold(self):
        ref, candidate = self.root / "ref.png", self.root / "candidate.png"
        Image.new("RGB", (48, 48), "black").save(ref)
        shutil.copy(ref, candidate)
        config = [{"id": "home", "kind": "image", "target_state": "home-48",
                   "reference": "ref.png", "candidate": "candidate.png", "max_rgb_mae": .2}]
        path = self.write_config(config)
        self.assertEqual(run_suite(path, self.root / "out")["status"],
                         "technical_checks_passed_manual_review_required")
        Image.new("RGB", (48, 48), "white").save(candidate)
        self.assertEqual(run_suite(path, self.root / "out")["status"], "failed")


class TestCaptureConfig(unittest.TestCase):
    def test_default_remote_url_denied(self):
        cfg = {"url": "https://example.com", "viewport": {"width": 390, "height": 844},
               "steps": [{"action": "screenshot"}]}
        with self.assertRaisesRegex(EvidenceError, "--allow-remote"):
            validate_config(cfg)
        validate_config(cfg, allow_remote=True)

    def test_unsafe_action_denied(self):
        cfg = {"url": "http://localhost:8000", "viewport": {"width": 390, "height": 844},
               "steps": [{"action": "evaluate", "value": "alert(1)"}]}
        with self.assertRaises(EvidenceError):
            validate_config(cfg)

    def test_local_url_checker_blocks_external_and_redirect_targets(self):
        self.assertTrue(is_local_url("http://localhost:8000"))
        self.assertTrue(is_local_url("http://127.0.0.1:8000/test"))
        self.assertFalse(is_local_url("https://localhost.evil.test/"))
        self.assertFalse(is_local_url("file:///tmp/index.html"))
        self.assertFalse(is_local_url("https://example.com/"))

    def test_malformed_wait_and_scroll_get_validation_errors(self):
        cfg = {"url": "http://localhost:8000", "viewport": {"width": 390, "height": 844},
               "steps": [{"action": "wait_ms", "value": "abc"}]}
        with self.assertRaisesRegex(EvidenceError, "wait_ms"):
            validate_config(cfg)
        cfg["steps"] = [{"action": "scroll", "pixels": 1_000_000}]
        with self.assertRaisesRegex(EvidenceError, "scroll"):
            validate_config(cfg)

    def test_credentials_in_url_are_rejected(self):
        cfg = {"url": "http://user:pass@localhost:8000", "viewport": {"width": 390, "height": 844},
               "steps": [{"action": "screenshot"}]}
        with self.assertRaisesRegex(EvidenceError, "giriş bilgisi"):
            validate_config(cfg)

    def test_missing_action_selector_denied(self):
        cfg = {"url": "http://localhost:8000", "viewport": {"width": 390, "height": 844},
               "steps": [{"action": "click"}]}
        with self.assertRaises(EvidenceError):
            validate_config(cfg)


if __name__ == "__main__":
    unittest.main()

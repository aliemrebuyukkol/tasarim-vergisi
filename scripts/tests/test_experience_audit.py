from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from experience_audit import audit  # noqa: E402

EXAMPLE = Path(__file__).resolve().parents[2] / "examples" / "pet-game-human-lens.json"


class ExperienceAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = json.loads(EXAMPLE.read_text(encoding="utf-8"))

    def test_valid_example(self):
        self.assertEqual(audit(self.base), [])

    def test_evidence_cannot_exceed_record(self):
        payload = copy.deepcopy(self.base)
        payload["claims"][0]["evidence_level"] = "E4"
        self.assertTrue(any("daha yüksek" in issue for issue in audit(payload)))

    def test_user_observation_needs_actual_study(self):
        payload = copy.deepcopy(self.base)
        payload["claims"][0]["type"] = "user_observation"
        self.assertTrue(any("E3" in issue for issue in audit(payload)))

    def test_three_contexts_required(self):
        payload = copy.deepcopy(self.base)
        payload["viewer_contexts"] = payload["viewer_contexts"][:2]
        self.assertTrue(any("en az üç" in issue for issue in audit(payload)))

    def test_duplicate_context_rejected(self):
        payload = copy.deepcopy(self.base)
        payload["viewer_contexts"][1]["id"] = payload["viewer_contexts"][0]["id"]
        self.assertTrue(any("tekrar eden bağlam" in issue for issue in audit(payload)))

    def test_ordered_moments(self):
        payload = copy.deepcopy(self.base)
        payload["moments"][1]["stage"] = "afterglow"
        self.assertTrue(any("beklenen interpretation" in issue for issue in audit(payload)))

    def test_counter_hypothesis_required(self):
        payload = copy.deepcopy(self.base)
        payload["moments"][2]["counter_hypothesis"] = ""
        self.assertTrue(any("counter_hypothesis" in issue for issue in audit(payload)))

    def test_surprise_must_change_expectation(self):
        payload = copy.deepcopy(self.base)
        payload["surprise"]["unexpected_change"] = payload["surprise"]["baseline_expectation"]
        self.assertTrue(any("beklenen ile beklenmedik aynı" in issue for issue in audit(payload)))

    def test_reduced_motion_is_required(self):
        payload = copy.deepcopy(self.base)
        payload["safety"]["reduced_motion"] = False
        self.assertTrue(any("reduced_motion" in issue for issue in audit(payload)))

    def test_test_plan_requires_open_question(self):
        payload = copy.deepcopy(self.base)
        payload["test_plan"]["non_leading_question"] = ""
        self.assertTrue(any("non_leading_question" in issue for issue in audit(payload)))

    def test_claim_source_must_match_record(self):
        payload = copy.deepcopy(self.base)
        payload["evidence_level"] = "E3"
        self.assertTrue(any("evidence_source" in issue for issue in audit(payload)))
        self.assertTrue(any("user_test_details" in issue for issue in audit(payload)))

    def test_bad_shape(self):
        self.assertTrue(audit([1, 2, 3]))


if __name__ == "__main__":
    unittest.main()

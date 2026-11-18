from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from idea_audit import audit  # noqa: E402


EXAMPLE = Path(__file__).resolve().parents[2] / 'examples' / 'pet-game-directions.json'


class CreativeAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = json.loads(EXAMPLE.read_text(encoding='utf-8'))

    def test_example_has_three_distinct_directions(self):
        self.assertEqual(audit(self.base), [])

    def test_reject_duplicate_ids(self):
        p = copy.deepcopy(self.base)
        p['directions'][1]['id'] = p['directions'][0]['id']
        self.assertTrue(any('tekrar eden' in item for item in audit(p)))

    def test_reject_cosmetic_clone(self):
        p = copy.deepcopy(self.base)
        for key in ('core_action', 'mechanic', 'composition', 'motion', 'emotional_payoff'):
            p['directions'][1][key] = p['directions'][0][key]
        self.assertTrue(any('yapısal eksenin' in item for item in audit(p)))

    def test_reject_same_mechanic_as_baseline(self):
        p = copy.deepcopy(self.base)
        p['directions'][0]['mechanic'] = p['baseline']['mechanic']
        self.assertTrue(any('baseline ile aynı' in item for item in audit(p)))

    def test_reject_malformed_score(self):
        p = copy.deepcopy(self.base)
        p['directions'][2]['scores']['novelty'] = 9
        self.assertTrue(any('1-5' in item for item in audit(p)))

    def test_reject_missing_risk(self):
        p = copy.deepcopy(self.base)
        p['directions'][2]['risks'] = []
        self.assertTrue(any('.risks' in item for item in audit(p)))

    def test_no_directions_is_error(self):
        p = copy.deepcopy(self.base)
        p['directions'] = []
        self.assertTrue(audit(p))


if __name__ == '__main__':
    unittest.main()

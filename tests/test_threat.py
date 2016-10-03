from unittest import *

from RiskCalculator import Threat


class ThreatTest(TestCase):
    def test_threat_level(self):
        t = Threat(type='test', critical=10, vulnerability=[{'name': '1', 'chance': 10}, {'name': '2', 'chance': 10}])
        self.assertAlmostEqual(t.threat_level, 0.36, delta=0.00000001)

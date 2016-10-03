from unittest import *

from RiskCalculator import Resource, Threat


class ResourceTest(TestCase):
    def test_threat_level(self):
        resource = Resource(name='Сервер', critical=56, threats=self.mock_threats())
        self.assertAlmostEqual(resource.threat_level, 0.5904, delta=0.0001)

    def test_str(self):
        resource = Resource(name='Сервер', critical=56, threats=self.mock_threats())
        print(str(resource))

    def mock_threats(self):
        param = [
            {
                "type": "угроза конфиденциальности",
                "critical": 10,
                "vulnerability": [
                    {
                        "name": "ПЭМИ",
                        "chance": 10
                    },
                    {
                        "name": "наводки на соседние линии",
                        "chance": 10
                    }
                ]
            },
            {
                "type": "угроза целостности",
                "critical": 10,
                "vulnerability": [
                    {
                        "name": "ошибки персонала",
                        "chance": 10
                    },
                    {
                        "name": "сбой оборудования",
                        "chance": 10
                    }
                ]
            }
        ]
        for p in param:
            yield Threat(**p)

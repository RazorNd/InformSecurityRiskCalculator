from functools import reduce

from RiskCalculator import Resource


class RiskCalculator:
    def __init__(self, resources):
        self.resources = []
        self.init_resources(resources)

    def init_resources(self, resources):
        for name, param in resources.items():
            self.resources.append(Resource(name=name, **param))

    @property
    def risk(self):
        return (1 - reduce(lambda r, x: r * (1 - (x.risk / 100)), self.resources, 1)) * 100

    def risk_str(self):
        return "Уровень риска для всех ресурсов: {risk:.4}".format(risk=self.risk)

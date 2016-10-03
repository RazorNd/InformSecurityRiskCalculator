from abc import ABCMeta, abstractmethod
from functools import reduce


class ThreatComposition(metaclass=ABCMeta):
    @abstractmethod
    def get_threats(self):
        """
        Возвращает перечисляемый тип объектов с свойством threat_level
        :rtype: list
        """

    def threat_level_calc_str(self):
        return "1 - " + " * ".join(["(1 - {:<6.3})".format(t.threat_level) for t in self.get_threats()])

    @property
    def threat_level(self):
        return 1 - reduce(lambda res, th: res * (1 - th.threat_level), self.get_threats(), 1)

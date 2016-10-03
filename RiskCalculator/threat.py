from RiskCalculator import ThreatComposition
from RiskCalculator.vulnerability import Vulnerability


class Threat(ThreatComposition):
    def __init__(self, type, critical, vulnerability):
        self.type = type
        self.critical = critical
        self.vulnerability = []
        self.init_vulnerability(vulnerability)

    def init_vulnerability(self, vulnerability):
        for v in vulnerability:
            if isinstance(v, dict):
                self.vulnerability.append(Vulnerability(critical=self.critical, **v))
            elif isinstance(v, v):
                self.vulnerability.append(v)
            else:
                raise TypeError("In class Resource param 'vulnerability' must be dict or Vulnerability type")

    def get_threats(self):
        return self.vulnerability

    def __str__(self):
        return "{name:<30}: {threat_level:>6.3} = {threat_level_calc_str}".format(
            name=self.type, threat_level=self.threat_level, threat_level_calc_str=self.threat_level_calc_str()
        )

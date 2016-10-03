from . import Threat, ThreatComposition


class Resource(ThreatComposition):
    def __init__(self, name, critical, threats):
        self.threats = []
        self.name = name
        self.critical = critical
        self.init_threats(threats)

    def init_threats(self, threats):
        for threat in threats:
            if isinstance(threat, dict):
                self.threats.append(Threat(**threat))
            elif isinstance(threat, Threat):
                self.threats.append(threat)
            else:
                raise TypeError("In class Resource param 'threats' must be dict or Threat type")

    def get_threats(self):
        return self.threats

    @property
    def risk(self):
        return self.threat_level * self.critical

    def __str__(self):
        return "{name} имеет уровень угрозы {threat_level:.3} = {threat_level_calc_str}, где: \n{threats}".format(
            threat_level_calc_str=self.threat_level_calc_str(),
            threats="\n".join([str(t) for t in self.threats]),
            name=self.name, threat_level=self.threat_level
        )

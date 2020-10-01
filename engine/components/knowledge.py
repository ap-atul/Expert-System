from engine.logger.logger import Log


class Rule:
    def __init__(self, rule: str):
        self.__rule = rule

    def getRule(self):
        return self.__rule


class Knowledge:
    def __init__(self):
        self.__target = None
        self.__rules = list()

    def addRule(self, target, rule):
        self.__target = target
        self.__rules.append(Rule(rule))

    def __str__(self):
        data = list()
        data.append(self.__target)
        data.append(" =====> \n")
        for rule in self.__rules:
            data.append("\t  <<< ")
            data.append(rule.getRule())
            data.append(" >>>  \n")
        data.append("\n\n")

        return "".join(data)

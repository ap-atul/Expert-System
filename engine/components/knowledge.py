from engine.logger.logger import Log
from engine.util.constants import PERCENT_MATCH


class Rule:
    def __init__(self, rule: str):
        self.__rule = rule

    def getRule(self):
        return self.__rule

    def __eq__(self, other):
        if other.__rule.__contains__(self.__rule):
            return True
        return False

    def __str__(self):
        return self.__rule


def sortDictionary(matchesRules):
    return {key: value for key, value in sorted(matchesRules.items(), key=lambda item: item[1], reverse=True)}


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

    def getTarget(self):
        return self.__target

    def getRules(self):
        return self.__rules

    def compareTo(self, knowledgeBase):
        matchesRules = dict()

        # getting each knowledge from the base
        for knowledge in knowledgeBase:
            match = 0

            # comparing each rule
            for rule in knowledge.getRules():
                for baseRule in self.__rules:
                    if rule == baseRule:
                        match += 1

            # adding the percent of match for each target
            matchesRules[knowledge.getTarget()] = (match / len(knowledge.getRules())) * 100

        # high percentage is returned based on satisfication of MATCH
        matchesRules = sortDictionary(matchesRules)
        Log.d(f"Matches :: {matchesRules}")
        for target, percent in matchesRules.items():
            if percent >= PERCENT_MATCH:
                return True, target + " " + str(percent) + " % sure"
            else:
                return False, target

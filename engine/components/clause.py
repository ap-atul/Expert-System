class Clause:
    def __init__(self):
        self.__clause = None
        self.__negative = None
        self.__positive = None

    def addClause(self, clause, negative, positive):
        self.__clause = clause
        self.__negative = negative
        self.__positive = positive

    def updateClause(self, clause):
        self.__clause = clause

    def delClause(self):
        self.__clause = None

    def getClause(self):
        return self.__clause

    def __str__(self):
        return self.__clause

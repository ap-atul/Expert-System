import os
import json

from engine.logger.logger import Log
from engine.components.clause import Clause


class ClauseParser:
    def __init__(self):
        self.__clauses = list()

    def __parseInputFile(self, inputFile):
        if os.path.isfile(inputFile) is False:
            Log.e(f"Clause file {inputFile} does not exists")
            return

        with open(inputFile, "r") as file:
            file = json.load(file)

            for clause in file:
                cl = Clause()
                cl.addClause(file[clause])
                self.__clauses.append(cl)

        return self.__clauses

    def getClauseBase(self, inputFile):
        return self.__parseInputFile(inputFile)

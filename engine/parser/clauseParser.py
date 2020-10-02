"""
Parser to parse the clause.json to retrieve the clause and its answers
"""

import json
import os

from engine.components.clause import Clause
from engine.logger.logger import Log


class ClauseParser:
    """
    Class to parse the json file to generate the Clause object lists
    for the run.

    Attributes
    ----------
    __clauses : list
        list of the Clause objects
    """

    def __init__(self):
        self.__clauses = list()

    def __parseInputFile(self, inputFile):
        """
        Read the `clause.json` and retrieve the question and the answers.

        Parameters
        ----------
        inputFile : str
            name and path of the file

        Returns
        -------
        list
            list of the Clause objects

        """
        # checking if the input file exists
        if os.path.isfile(inputFile) is False:
            Log.e(f"Clause file {inputFile} does not exists")
            return

        # reading the file
        with open(inputFile, "r") as file:
            file = json.load(file)

            # reading the que and ans, appending to a list
            for clause in file:
                cl = Clause()
                cl.addClause(
                    clause=file[clause]['question'],
                    negative=file[clause]['answer']['negative'],
                    positive=file[clause]['answer']['positive']
                )
                self.__clauses.append(cl)

        return self.__clauses

    def getClauseBase(self, inputFile):
        """
        Function call to parse the input file and generate a list
        of Clauses

        Parameters
        ----------
        inputFile : str
            name and path of the clause.json

        Returns
        -------
        list
            list of the Clause objects
        """
        return self.__parseInputFile(inputFile)

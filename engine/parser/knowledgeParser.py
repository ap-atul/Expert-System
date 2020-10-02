"""
This file will parse the input text file and get important
knowledge from it and create a database known as Knowledge Base
"""

import json
import os

from engine.components.knowledge import Knowledge
from engine.logger.logger import Log


class KnowledgeBaseParser:
    """
    Class the parse the file and create the Knowledge object list

    Attributes
    ----------
    __knowledgeBase : list
        list of the Knowledge objects
    """

    def __init__(self):
        self.__knowledgeBase = list()

    def __parseInputFile(self, inputFile):
        """
        Reads the `knowledge.json` and retrieves the target and the rules for the target

        Parameters
        ----------
        inputFile : str
            name and path of the file to parsse

        Returns
        -------
        list
            list of the Knowledge objects
        """
        # checking if the file exists
        if os.path.isfile(inputFile) is False:
            Log.e(f"Knowledge file {inputFile} does not exists")
            return

        # reading the file
        with open(inputFile, "r") as file:
            file = json.load(file)

            for knowledge in file['target']:
                knowledgeBase = Knowledge()
                for rule in knowledge['rules']:
                    knowledgeBase.addRule(target=knowledge['name'],
                                          rule=knowledge['rules'][rule])
                self.__knowledgeBase.append(knowledgeBase)

        return self.__knowledgeBase

    def getKnowledgeBase(self, inputFile):
        """
        Parsing the input file and returning the list

        Parameters
        ----------
        inputFile : str
            name and path of the file to parse

        Returns
        -------
        list
            list of the Knowledge objects
        """
        return self.__parseInputFile(inputFile)

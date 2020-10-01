import os
import json

from engine.logger.logger import Log
from engine.components.knowledge import Knowledge

"""
This file will parse the input text file and get important
knowledge from it and create a database known as Knowledge Base
"""


class KnowledgeBaseParser:
    def __init__(self):
        self.__knowledgeBase = list()

    def __parseInputFile(self, inputFile):
        if os.path.isfile(inputFile) is False:
            Log.e(f"Knowledge file {inputFile} does not exists")
            return

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
        return self.__parseInputFile(inputFile)

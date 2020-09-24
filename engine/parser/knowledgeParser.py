import os
import json

from engine.logger.logger import Log

"""
This file will parse the input text file and get important
knowledge from it and create a database known as Knowledge Base
"""


class KnowledgeBaseParser:
    def __init__(self):
        self.inputFile = None
        self.targetNames = list()
        self.targetComponents = list()

    def parseInputFile(self, inputFile):
        self.inputFile = inputFile

        if os.path.isfile(inputFile) is False:
            Log.e(f"Knowledge file {inputFile} does not exists")

        with open(inputFile, "r") as file:
            file = json.load(file)




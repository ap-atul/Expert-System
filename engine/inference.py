import os

from engine.components.knowledge import Knowledge, Rule
from engine.logger.logger import Log
from engine.parser.clauseParser import ClauseParser
from engine.parser.knowledgeParser import KnowledgeBaseParser
from engine.util.constants import USER_INPUT_SEP, AVATAR


class Inference:
    def __init__(self):
        self.__knowledgeParser = KnowledgeBaseParser()
        self.__clauseParser = ClauseParser()

        self.__knowledgeBase = None
        self.__clauseBase = None

    def startEngine(self, knowledgeBase, clauseBase):
        if not os.path.isfile(knowledgeBase):
            Log.e(f"The knowledge file {knowledgeBase} does not exists.")
        if not os.path.isfile(clauseBase):
            Log.e(f"The clause file {clauseBase} does not exists.")

        Log.d("Parsing the files to generate a Knowledge Base...")
        self.__knowledgeBase = self.__knowledgeParser.getKnowledgeBase(knowledgeBase)
        self.__clauseBase = self.__clauseParser.getClauseBase(clauseBase)

        self.__askQuestion()

    def __askQuestion(self):
        for clause in self.__clauseBase:
            print()
            userInput = input(Log.modes['WARN'] + AVATAR + " >>> " + clause.getClause() + "\n You >>> ").strip()
            output = self.__inferenceResolve(userInput)
            if output[0]:
                Log.i(clause.getPositive() + output[1])
            else:
                Log.i(clause.getNegative() + output[1])

        Log.i("Hope that you are satisfied with your answers !")

    def __inferenceResolve(self, userInput):
        userInputs = userInput.split(USER_INPUT_SEP)
        print(userInputs)
        userKnowledge = Knowledge()

        # creating a knowledge base of the user input
        for userIn in userInputs:
            userKnowledge.addRule("user", userIn)

        return userKnowledge.compareTo(self.__knowledgeBase)





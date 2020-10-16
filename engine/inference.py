"""
Inference Engine to run the forward and backward chaining on the parsed
KnowledgeBase and ClauseBase
"""

import os

from engine.components.knowledge import Knowledge
from engine.logger.logger import Log
from engine.parser.clauseParser import ClauseParser
from engine.parser.knowledgeParser import KnowledgeBaseParser
from engine.util.constants import USER_INPUT_SEP, AVATAR, PERCENT_MATCH
from engine.util.utilities import sortDictionary


class Inference:
    """
    Inference parses the input files and creates KnowledgeBase and ClauseBase that can be
    used for forward and backward chaining

    Attributes
    -----------
    __knowledgeParser : KnowledgeBaseParser
        parser to parse the knowledge file into objects
    __clauseParser : ClauseParser
        parser to parse the clause file into objects
    __knowledgeBase : list
        list of parsed Knowledge objects
    __clauseBase : list
        list of parsed Clause objects
    __verbose : bool
        to print the matched values percents
    __method : str
        values accepted

            forward : run forward chaining
            backward : run backward chaining

    """

    def __init__(self):
        self.FORWARD = "forward"
        self.BACKWARD = "backward"

        self.__knowledgeParser = KnowledgeBaseParser()
        self.__clauseParser = ClauseParser()

        self.__knowledgeBase = None
        self.__clauseBase = None
        self.__verbose = None
        self.__method = None

    def startEngine(self, knowledgeBase, clauseBase, verbose=False, method="forward"):
        """
        Read the files to parse and other options. Initialize the parsers and get the parsed values

        Parameters
        ----------
        knowledgeBase : str
            name and path of the file
        clauseBase : str
            name and path of the file
        verbose : bool, default=False
            to print extra details
        method : str, default="forward"
            method to run on

        """
        if not os.path.isfile(knowledgeBase):
            Log.e(f"The knowledge file {knowledgeBase} does not exists.")
        if not os.path.isfile(clauseBase):
            Log.e(f"The clause file {clauseBase} does not exists.")

        Log.d("Parsing the files to generate a Knowledge Base...")
        self.__knowledgeBase = self.__knowledgeParser.getKnowledgeBase(knowledgeBase)
        self.__clauseBase = self.__clauseParser.getClauseBase(clauseBase)
        self.__verbose = verbose
        self.__method = method

        # asking the questions from the Clause base
        self.__askQuestion()

    def __askQuestion(self):
        """
        Ask the question iteratively from the Clause base
        """
        for clause in self.__clauseBase:
            print()
            userInput = input(Log.modes['WARN'] + AVATAR + " >>> " + clause.getClause() + "\nYou >>> ").strip()
            output = self.__inferenceResolve(userInput)
            if output[0]:
                Log.i(clause.getPositive() + output[1])
            else:
                Log.i(clause.getNegative() + output[1])

        Log.i("Hope that you are satisfied with your answers !")

    def __inferenceResolve(self, userInput):
        """
        Run the inference on the user input for each clause. Method attribute determines
        the method being used

        Parameters
        ----------
        userInput : str
            input from the user

        Returns
        -------
        tuple
            bool : True for finding a match and string : A formatted string with target and percentage

        """
        userInputs = userInput.split(USER_INPUT_SEP)
        userKnowledge = Knowledge()

        # creating a knowledge base of the user input
        for userIn in userInputs:
            userKnowledge.addRule("user", userIn)

        # run inference with selected method
        if self.__method == "forward":
            return self.__runForwardChain(userKnowledge)
        else:
            return self.__runBackwardChain(userKnowledge)

    def __runForwardChain(self, userBase):
        """
        Running forward chaining.Steps are as follows :

            1. Match each user rule with all the rules for each Knowledge target
            2. Calculate the percentage for each target
            3. Return the output for the percent that satisfies the Min percent
            4. If verbose is True, print all matches with percentages

        Parameters
        ----------
        userBase : Knowledge
            Knowledge object created by parsing the user input

        Returns
        -------
        tuple
            bool : True denoting match found; str : formatted target name and percentage
        """
        matchesRules = dict()

        # getting each knowledge from the base
        for knowledge in self.__knowledgeBase:
            match = 0

            # comparing each rule
            for rule in knowledge.getRules():
                for userRule in userBase.getRules():
                    if rule == userRule:
                        match += 1

            # adding the percent of match for each target
            matchesRules[knowledge.getTarget()] = (match / len(knowledge.getRules())) * 100

        # high percentage is returned based on satisfaction of MATCH
        matchesRules = sortDictionary(matchesRules)

        if self.__verbose:
            for target, percent in matchesRules.items():
                Log.d(f"Target :: {target} --->  Matched :: {percent}")
            print()

        # returning the first match if it greater than the MIN
        for target, percent in matchesRules.items():
            if percent >= PERCENT_MATCH:
                return True, target + " " + str(percent) + " % sure"
            else:
                return False, target

    def __runBackwardChain(self, userBase: Knowledge):
        """
        Running forward chaining.Steps are as follows :

            1. Scan the Knowledge Base rules with the user rule
            2. When match is found, save the Knowledge target as new target
            3. Run match on the selected targets
            4. Return the output based on the Min percent

        Parameters
        ----------
        userBase : Knowledge
            Knowledge object created by parsing the user input

        Returns
        -------
        tuple
            bool : True denoting match found; str : formatted target name and percentage
        """
        matchedTargets = list()
        matchesRules = dict()

        # finding initial target
        for knowledge in self.__knowledgeBase:
            for rule in knowledge.getRules():
                for userRule in userBase.getRules():
                    # rule match target acquired
                    if rule == userRule:
                        matchedTargets.append(knowledge)
                        break

        # running matching on the selected targets
        for matchedTarget in matchedTargets:
            match = 0
            for rule in matchedTarget.getRules():
                for userRule in userBase.getRules():
                    if rule == userRule:
                        match += 1

            # saving the target with its percent match
            matchesRules[matchedTarget.getTarget()] = (match / len(matchedTarget.getRules())) * 100

        # sorting the matched rules by the percentages
        matchesRules = sortDictionary(matchesRules)

        if self.__verbose:
            for target, percent in matchesRules.items():
                Log.d(f"Target :: {target} --->  Matched :: {percent}")
            print()

        # returning the highest matches target if is greater than the MIN
        for target, percent in matchesRules.items():
            if percent >= PERCENT_MATCH:
                return True, target + " " + str(percent) + " % sure"
            else:
                return False, target

"""
Clauses parsing from the clause.json file. This refers to questions
asked by the engine. Answers are two types

    positive : on rule match
    negative : on no rule match

"""


class Clause:
    """
    Clause refers to question asked. The rules are matches with the
    answers given by the user for the clause.
    The answer can be statements separated by the SEP in `constants` file

    Attributes
    ----------
    __clause : str
        the original question
    __negative : str
        negative answer for the question
    __positive : str
        positive answer for the question

    """

    def __init__(self):
        self.__clause = None
        self.__negative = None
        self.__positive = None

    def addClause(self, clause, negative, positive):
        """
        Creating a clause by the taking the question in the input and
        using the positive and negative statements to create the
        Clause object

        Parameters
        ----------
        clause : str
            question
        negative : str
            negative answer for the clause
        positive : str
            positive answer for the clause

        """
        self.__clause = clause
        self.__negative = negative
        self.__positive = positive

    def updateClause(self, clause):
        """
        Utility function to update the clause question

        Parameters
        ----------
        clause : str
            new question

        """
        self.__clause = clause

    def delClause(self):
        """
        Deleting the question
        """
        self.__clause = None

    def getClause(self):
        """
        Get the clause, question

        Returns
        -------
        str
            question
        """
        return self.__clause

    def getPositive(self):
        """
        Get the positive answer

        Returns
        -------
        str
            positive answer

        """
        return self.__positive

    def getNegative(self):
        """
        Get the negative answer

        Returns
        -------
        str
            negative answer

        """
        return self.__negative

    def __str__(self):
        """
        Print the question
        """
        return self.__clause

"""
The parsed output of the knowledge,json is used to create
the Knowledge object consisting of the target and rules
"""


class Rule:
    """
    Class to store the rule in the string format

    Attributes
    -----------
    __rule: str
        rule for the knowledge
    """

    def __init__(self, rule: str):
        self.__rule = rule

    def getRule(self):
        """
        Get the rule

        Returns
        -------
        str
            rule of the current object
        """
        return self.__rule

    def __eq__(self, other):
        """
        Comparison of two rules. Substring and more complex
        comparison

        Parameters
        ----------
        other : Rule
            object of the Rule

        Returns
        -------
        bool
            True if a match
        """
        if other.__rule.__contains__(self.__rule):
            return True
        return False

    def __str__(self):
        """
        Print the rule string

        Returns
        -------
        str
            rule
        """
        return self.__rule


class Knowledge:
    """
    Class that connects the target with the rules (Rule objects).

    Attributes
    ----------
    __target : str
        name of the target or the output
    __rules : list
        list of the Rule objects

    """

    def __init__(self):
        self.__target = None
        self.__rules = list()

    def addRule(self, target, rule):
        """
        Add new rule to the Knowledge

        Parameters
        ----------
        target : str
            output or the name of the target
        rule : str
            rule for the Knowledge
        """
        self.__target = target
        self.__rules.append(Rule(rule))

    def __str__(self):
        """
        Printing the knowledge base with some formatting

        Returns
        -------
        str
            put together string
        """
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
        """
        Get the name of the output

        Returns
        -------
        str
            name of the target
        """
        return self.__target

    def getRules(self):
        """
        Get the list of all the rules of the Knowledge

        Returns
        -------
        list
            all rules
        """
        return self.__rules

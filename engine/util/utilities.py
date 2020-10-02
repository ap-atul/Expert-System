def sortDictionary(matchesRules):
    """
    sort the dictionary by the values

    Parameters
    ----------
    matchesRules : dict
        input dictionary

    Returns
    -------
    dict
        sorted by values dictionary
    """
    return {key: value for key, value in sorted(matchesRules.items(), key=lambda item: item[1], reverse=True)}

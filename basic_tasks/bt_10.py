# from pprint import pprint


def charFreq(_str):
    return {i: _str.count(i) for i in list(set(_str))}


# pprint(charFreq("abbabcbdbabdbdbabababcbcbab"), width=1)

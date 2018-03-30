from pprint import pprint


def charFreq(_str):
    return {i: _str.count(i) for i in list(set(_str))}


freq_str = "abbabcbdbabdbdbabababcbcbab"
pprint(charFreq(freq_str), width=1)

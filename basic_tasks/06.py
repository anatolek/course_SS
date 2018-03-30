from string import printable


def caesarCipher(_str, _key):
    # "printable" string has length 100 characters

    if not (-99 < _key < 99):
        return "The '_key' value must be in range -99...99"

    # create the encoded alphabetical string
    enc_str = "".join(list(printable)[_key:] + list(printable)[:_key])

    # create Caesar dictionary
    _dict = dict(zip(list(printable), list(enc_str)))

    # create the encoded string
    j = ""
    for i in _str:
        j = j+_dict[i]

    return j


print(caesarCipher("My name is Anatolii", 7))

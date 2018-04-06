def close_brackets(_str):
    if len(_str) % 2 != 0:
        return "NOT OK"

    ok = 0
    for i in _str:
        if i == '[' and ok >= 0:
            ok += 1
        elif ok >= 0:
            ok -= 1
        else:
            return "NOT OK"
    if ok == 0:
        return "OK"
    return "NOT OK"


# OK
print(close_brackets("[]"))
print(close_brackets("[][]"))
print(close_brackets("[[][]]"))
# NOT OK
print(close_brackets("]["))
print(close_brackets("][]["))
print(close_brackets("[]][[]"))

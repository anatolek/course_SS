def isPalindrome(_str):
    return _str == "".join(list(_str)[::-1])


print(isPalindrome("radar"))
print(isPalindrome("radar1"))

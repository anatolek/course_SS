def _sum(arr):
    j = 0
    for i in arr:
        j = i + j
    return j


def _multiply(arr):
    j = 1
    for i in arr:
        j = i * j
    return j


print(_sum([1, 2, 3, 4]))
print(_multiply([1, 2, 3, 4]))

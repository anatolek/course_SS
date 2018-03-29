def diagonalReverse(_list):
    k = 0
    j = []
    for i in _list:
        j.append([l for l in i])
        k += 1
    return j


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(diagonalReverse(matrix))

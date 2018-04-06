def decToBin(_num):
    _bin = ""
    while _num > 0:
        if _num % 2 == 0:
            _bin += "0"
        else:
            _bin += "1"
        _num //= 2
    return _bin

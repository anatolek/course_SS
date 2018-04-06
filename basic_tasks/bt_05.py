from time import sleep


def histogram(_arr):
    for i in _arr:
        for j in range(i):
            print("*", end='', flush=True)
            sleep(.250)
        # move to a new line
        print("")


histogram([4, 9, 7])

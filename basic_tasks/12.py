from random import randint
from pprint import pprint


def rand_matrix(order):
    matrix = [[0 for col in range(order)] for row in range(order)]
    matrix[randint(0, order-1)][randint(0, order-1)] = 1
    return matrix


def coord_list(order):
    num = input("Enter 'x y' in range 1..." + str(order) + ": ")
    return [int(i) - 1 for i in num.split()]


def game(order):
    mx = rand_matrix(order)
    shot_mx = [[0 for col in range(order)] for row in range(order)]
    xy = coord_list(order)
    shot_mx[xy[0]][xy[1]] = 8
    pprint(shot_mx, width=3*order+2)
    while mx[xy[0]][xy[1]] != 1:
        print("\nTry again!")
        xy = coord_list(order)
        shot_mx[xy[0]][xy[1]] = 8
        pprint(shot_mx, width=3 * order + 2)
    shot_mx[xy[0]][xy[1]] = 1
    print('\nGreat!!!\n')
    pprint(shot_mx, width=3 * order + 2)
    print("You won, you are the best!!!")


game(2)
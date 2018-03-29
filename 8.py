from random import randint


def game(r1, r2):
    x = randint(r1, r2)
    #print("The guessed number is ", x)
    num = input("Enter a number: ")
    while int(num) != x:
        print("Try again!")
        num = input("Enter a number: ")
    print("You won, you are the best!!!")


game(10, 15)

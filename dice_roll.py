"""The program should do the following:

Randomly roll a pair of dice
Add the values of the roll
Ask the user to guess a number
Compare the user's guess to the total value
Decide a winner (the user or the program)
Inform the user who the winner is"""
from random import randint
from time import sleep




def get_user_guess():
    user_guess = int(raw_input("Guess a number: "))
    return user_guess
def roll_dice(number_of_sides):
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    max_val = number_of_sides * 2
    print('The maximum possible value is: ' + str(max_val))
    sleep(1)
    user_guess = get_user_guess()
    if user_guess > max_val:
        print("No guessing higher tahn the maximun possible value")
        return
    else:
        print("Rolling...")
        sleep(2)
        print("The first value is: %d" % first_roll)
        sleep(1)
        print("The second value is: %d" % second_roll)
        sleep(1)
        total_roll = first_roll + second_roll
        print("The first value is: %d" % first_roll)
        print("Result...")
        sleep(1)
        if user_guess > total_roll:
            print("You win!!")
            return
        else:
            print("You lose!!")
            return
roll_dice(6)
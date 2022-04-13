from random import randint
"""
Alex James
lab12.py
Problem: Create functions using while loops.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def find_and_remove_first(search_list, value):
    searching = True
    count = 0
    while searching:
        searching = search_list[count]
        if searching == value:
            search_list.remove(search_list[count])
            search_list.insert(count, "Alex")
            searching = False
        count += 1
    print(search_list)


def good_input():
    user_input = -1
    while not (10 > user_input > 0):
        user_input = eval(input("Enter a number 1 through 10."))
        if user_input > 10:
            print("Your number is too high. Enter a number that is 10 or less.")
        elif user_input < 0:
            print("Your number is too low. Enter a number that is 0 or greater.")
    return user_input


def num_digits():
    user_input = "1"
    while eval(user_input) > 0:
        num_of_digits = 0
        testing_character = "1"
        user_input = input("Enter a number to find its number of digits. Enter 0 or below to quit.")
        user_input = user_input.strip()
        user_input = user_input + " "
        while testing_character != " ":
            testing_character = user_input[num_of_digits]
            num_of_digits += 1
        if eval(user_input) > 0:
            print("There are {} digits in that number.".format(num_of_digits - 1))


def hi_lo_game():
    guesses_remain = 7
    rand_num = randint(1, 100)
    guesses_taken = 0
    while guesses_remain > 0:
        guess = eval(input("Enter a number 1 through 100 to guess."))
        guesses_remain -= 1
        guesses_taken += 1
        if guess > rand_num:
            print("Your guess is too high.")
        elif guess < rand_num:
            print("Your guess is too low.")
        elif guess == rand_num:
            print("You won. It took you {} guesses.".format(guesses_taken))
            guesses_remain = 0
            guesses_taken = 0
    if guesses_taken > 1:
        print("You lost. The correct number was {}.".format(rand_num))

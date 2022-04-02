from random import randint
from graphics import Point, GraphWin, Circle, Text, Line, Entry

"""
Name: Alex James
hw9.py
Problem: Create 2 versions of the game Hangman.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def get_words(file_name):
    file = open(file_name, 'r')
    return file.readlines()


def get_random_word(words):
    new_string = ""
    for word in words:
        new_string = new_string + word
    new_string.strip()
    new_list = new_string.split("\n")
    new_list.remove("")
    random_num = randint(0, (len(new_list) - 1))
    return new_list[random_num]


def letter_in_secret_word(letter, secret_word):
    found = secret_word.find(letter)
    if found == -1:
        return False
    return True


def already_guessed(letter, guesses):
    is_guessed = guesses.count(letter)
    if is_guessed > 0:
        return True
    return False


def make_hidden_secret(secret_word, guesses):
    return_string = ""
    for letter in secret_word:
        is_guessed = guesses.count(letter)
        if is_guessed > 0:
            return_string += letter + " "
        else:
            return_string += "_ "
    return_string = return_string.strip()
    return return_string


def won(guessed):
    for letter in guessed:
        if letter == "_":
            return False
    return True


def play_command_line(secret_word):
    guessed_letters = []
    guesses_remaining = 6
    word_display = make_hidden_secret(secret_word, guessed_letters)
    while guesses_remaining > 0:
        print("Already guessed: ", end="")
        print(guessed_letters)
        print("Guesses remaining: " + str(guesses_remaining))
        print(word_display)
        new_letter = input("Guess a letter:")
        if not already_guessed(new_letter, guessed_letters):
            guessed_letters.append(new_letter)
            if letter_in_secret_word(new_letter, secret_word):
                word_display = make_hidden_secret(secret_word, guessed_letters)
            else:
                guesses_remaining -= 1
            if won(word_display):
                print("winner!")
                print(secret_word)
                guesses_remaining = 0
            else:
                print("")
    if not won(word_display):
        print("sorry. you did not guess the word.")
        print("the secret word was " + secret_word)


def play_graphic_interface(secret_word):
    guessed_letters = []
    guesses_remaining = 6
    word_display = make_hidden_secret(secret_word, guessed_letters)
    gui = GraphWin("Hangman", 750, 750)
    gallows = [Line(Point(300, 460), Point(540, 460)), Line(Point(420, 460), Point(420, 120)),
               Line(Point(210, 120), Point(420, 120)), Line(Point(210, 120), Point(210, 150))]
    body = [Circle(Point(210, 190), 40), Line(Point(210, 230), Point(210, 450)),
            Line(Point(210, 240), Point(360, 360)), Line(Point(210, 240), Point(60, 360)),
            Line(Point(210, 450), Point(360, 600)), Line(Point(210, 450), Point(60, 600))]
    for piece in gallows:
        piece.draw(gui)
    guessed_letter_header = Text(Point(500, 400), "Guessed Letters:")
    guessed_letter_box = Text(Point(585, 420), "")
    inputting_letter_header = Text(Point(420, 490), "Input a letter:")
    input_box = Entry(Point(420, 510), 5)
    hidden_word_graphic = Text(Point(530, 510), word_display)
    result = Text(Point(420, 550), "")
    guessed_letter_header.draw(gui)
    inputting_letter_header.draw(gui)
    hidden_word_graphic.draw(gui)
    input_box.draw(gui)
    while guesses_remaining > 0:
        gui.getMouse()
        new_letter = input_box.getText()
        if not already_guessed(new_letter, guessed_letters):
            guessed_letter_box.undraw()
            guessed_letters.append(new_letter)
            guessed_letter_box.setText(guessed_letters)
            guessed_letter_box.draw(gui)
            if letter_in_secret_word(new_letter, secret_word):
                hidden_word_graphic.undraw()
                word_display = make_hidden_secret(secret_word, guessed_letters)
                hidden_word_graphic.setText(word_display)
                hidden_word_graphic.draw(gui)
            else:
                guesses_remaining -= 1
                body[abs(guesses_remaining - 5)].draw(gui)
            if won(word_display):
                guesses_remaining = 0
                result.setText("winner!")
                input_box.undraw()
                inputting_letter_header.undraw()
                result.draw(gui)
    if not won(word_display):
        result.setText("sorry you did not win.\nthe correct word was {}".format(secret_word))
        result.draw(gui)
        input_box.undraw()
        inputting_letter_header.undraw()
    gui.getMouse()
    gui.close()

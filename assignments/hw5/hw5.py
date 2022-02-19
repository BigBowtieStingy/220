"""
Name: Alex James
hw5.py
Problem: Create programs that use
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def name_reverse():
    name = input("Enter a name (first last)")
    # Split at the blank space between first and last name
    name_table = name.split(" ")
    # Create a new string using entries from the created table and print it
    new_name = (name_table[1] + ", " + (name_table[0]))
    print(new_name)


def company_name():
    internet_domain = input("Enter a company's internet domain")
    # Use .split to seperate the name from "www." and ".com"
    name_table = internet_domain.split(".")
    # Get the text in the middle, then print it
    new_name = name_table[1]
    print(new_name)


def initials():
    num_of_students = eval(input("How many students are in the class?"))
    # Loop for the number of students
    for i in range(num_of_students):
        input_message = "What is the name of student " + str(i + 1) + "?"
        student_name = input(input_message)
        # Find the empty space, and then print the character 1 space after it for last initial
        space_location = student_name.find(" ")
        print(student_name[0] + student_name[space_location + 1])


def names():
    student_names = input("Enter a list of names seperated by commas:")
    student_table = student_names.split(", ")
    # Loop for the number of names inputted
    for student_name in student_table:
        # Find the empty space, and then print the character 1 space after it for last initial
        space_location = student_name.find(" ")
        print(student_name[0] + student_name[space_location + 1], end=" ")


def thirds():
    num_of_sentences = eval(input("How many sentences will be input?"))
    sentence_table = []
    for i in range(num_of_sentences):
        input_message = "Enter sentence " + str(i + 1) + ":"
        sentence = input(input_message)
        # Append the sentence to the list for later
        sentence_table.append(sentence)
    for current_sentence in sentence_table:
        # Create loop that will add each sentence's 3rd, 6th, 9th, etc. character
        letter_string = ""
        for i in range(0, len(current_sentence), 3):
            letter_string = letter_string + current_sentence[i]
        print(letter_string)


def word_average():
    sentence = input("Enter a sentence:")
    letter_total = 0
    word_total = 0
    word_table = sentence.split(" ")
    # Add to total values for each word
    for word in word_table:
        letter_total = len(word) + letter_total
        word_total = 1 + word_total
    print(letter_total / word_total)


def pig_latin():
    sentence = input("Enter a sentence to convert to pig Latin:")
    word_table = sentence.split(" ")
    pig_latin_sentence = ""
    for word in word_table:
        # Copy first character, and then remove it from the front
        new_word = word + word[0]
        new_word = new_word[1:(len(new_word) + 1)]
        # Add ay and make the word lowercase
        new_word = new_word + "ay"
        new_word = new_word.lower()
        # Store each word of pig latin into a new sentence
        pig_latin_sentence = pig_latin_sentence + new_word + " "
    # Use .rstrip() to remove the ending space
    print(pig_latin_sentence.rstrip())


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass

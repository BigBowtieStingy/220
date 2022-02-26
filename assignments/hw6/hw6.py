"""
Name: Alex James
hw5.py
Problem: Create programs that use string methods and functions
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def cash_converter():
    cash_amount = eval(input("Enter an integer:"))
    print("That is ${:.2f}".format(cash_amount))


def encode():
    message = input("Enter a message:")
    key = eval(input("Enter a key:"))
    # Convert each character into a number, add the key, and turn it back into a character
    encrypted_message = ""
    for character in message:
        character = ord(character) + key
        encrypted_message = encrypted_message + chr(character)
    print(encrypted_message)


def sphere_area(radius):
    area = 4 * math.pi * math.pow(radius, 2)
    return area


def sphere_volume(radius):
    volume = (4 / 3) * math.pi * math.pow(radius, 3)
    return volume


def sum_n(number):
    number_sum = 0
    for i in range(1, number + 1):
        number_sum = number_sum + i
    return number_sum


def sum_n_cubes(number):
    cube_sum = 0
    for i in range(1, number + 1):
        cube_sum = cube_sum + math.pow(i, 3)
    return cube_sum


def encode_better():
    message = input("Enter a message:")
    key = input("Enter a key:")
    key_length = len(key)
    key_start = 0
    encrypted_message = ""
    for letter in message:
        # Get both the encrypted letter and key, subtract by 65 to line them up with range
        encrypted_letter = ord(letter) - 65
        encrypted_key = ord(key[key_start]) - 65
        # Update the key loop
        key_start = key_start + 1
        # Restart key loop if it reaches its end
        key_start = (key_start % key_length)
        # Add the characters together and put results into message
        encrypted_total = (encrypted_letter + encrypted_key) % 58
        encrypted_message = encrypted_message + chr(encrypted_total + 65)
    print(encrypted_message)


if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass

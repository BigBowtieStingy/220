"""
Name: Alex James
hw7.py
Problem: Create programs that use functions and writing to files.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from encryption import encode, encode_better


def number_words(in_file_name, out_file_name):
    # Open both files, read the in_file
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')
    message_lines = in_file.readlines()
    new_message_table = []
    num_index = 1
    number_table = []
    for message_line in message_lines:
        for word in message_line.split(" "):
            # For each word, add it to a new table and add a cooresponding number
            new_message_table.append(word.replace("\n", ""))
            number_table.append(num_index)
            num_index = num_index + 1
    length = len(new_message_table)
    # For each word, write its number then the word to the out_file
    for i in range(length):
        new_message = new_message_table[i]
        new_number = str(number_table[i])
        output_message = new_number + " " + new_message
        print(output_message, file=out_file)
    # Close both files
    in_file.close()
    out_file.close()


def hourly_wages(in_file_name, out_file_name):
    # Open both files, read lines of in_file
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')
    message_lines = in_file.readlines()
    name_list = []
    pay_list = []
    for line in message_lines:
        line = line.replace("\n", "")
        words = line.split(" ")
        # The first two entries are the first and last name
        name_list.append(words[0] + " " + words[1])
        # Apply bonus
        bonus = 1.65
        # Third entry is hourly wage, fourth is hours worked
        pay = (eval(words[2]) + bonus) * eval(words[3])
        pay_list.append("{:.2f}".format(pay))
    length = len(pay_list)
    # For each employee, write their name and then their pay to the file
    for i in range(length):
        output_message = name_list[i] + " " + str(pay_list[i])
        print(output_message, file=out_file)
    # Close both files after the out_file was written to
    in_file.close()
    out_file.close()


def calc_check_sum(isbn):
    # Split the table at dashes and recombine it as new_isbn
    isbn_table = isbn.split("-")
    new_isbn = ""
    i = 10
    final_sum = 0
    for entry in isbn_table:
        new_isbn = new_isbn + entry
    # Calculate the sum, as i decreases by 1 each iteration
    for number in new_isbn:
        final_sum = (eval(number) * i) + final_sum
        i = i - 1
    return final_sum


def send_message(file_name, friend_name):
    # Open the file and the friend's name file
    opened_file = open(file_name, 'r')
    lines = opened_file.read()
    message_name = friend_name + ".txt"
    write_to_file = open(message_name, 'w')
    # Write the contents of the file to the friend's name file
    print(lines, file=write_to_file, end="")
    # Close both files
    opened_file.close()
    write_to_file.close()


def send_safe_message(file_name, friend_name, key):
    # Open the three files, and write to the friend's name file
    opened_file = open(file_name, 'r')
    lines = opened_file.readlines()
    message_name = friend_name + ".txt"
    write_to_file = open(message_name, 'w')
    # Encrypt each line individually, and remove new line characters with .replace
    for line in lines:
        line = line.replace("\n", "")
        # Call encode, final message is the encrypted line which is written to file
        final_message = encode(line, key)
        print(final_message, file=write_to_file)
    # Close both files after the friend's name file has been written to
    opened_file.close()
    write_to_file.close()


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    # Open the three files, and write to the friend's name file
    opened_file = open(file_name, 'r')
    pad_file = open(pad_file_name, 'r')
    key = pad_file.read()
    message_name = friend_name + ".txt"
    write_to_file = open(message_name, 'w')
    message = opened_file.read()
    # Call encode_better, final_message is the returned encrypted message
    final_message = encode_better(message, key)
    print(final_message, file=write_to_file)
    # Close files after writing to the friend's name file
    opened_file.close()
    write_to_file.close()
    pad_file.close()


if __name__ == '__main__':
    pass

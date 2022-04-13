"""
Alex James
algorithms.py
Problem: Create two algorithm functions using while loops.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def read_data(filename):
    nums_file = open(filename, 'r')
    line = nums_file.readline()
    num_list = []
    while line:
        line.replace("\n", "")
        line.strip()
        nums = line.split(" ")
        i = 0
        while i < len(nums):
            num_list.append(eval(nums[i]))
            i += 1
        line = nums_file.readline()
    nums_file.close()
    return num_list


def is_in_linear(search_val, values):
    searching = True
    not_failed = True
    found = False
    count = 0
    while searching and not_failed:
        searching = not values[count] == search_val
        if count == (len(values) - 1) and searching:
            not_failed = False
        elif not searching:
            found = True
        count += 1
    return found

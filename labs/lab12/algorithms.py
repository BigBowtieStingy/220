from graphics import Point, Rectangle
"""
Alex James
algorithms.py
Problem: Create algorithm functions using while loops.
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


def is_in_binary(search_val, values):
    left_index = 0
    right_index = len(values) - 1
    found = False
    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        middle_val = values[middle_index]
        print(middle_val)
        if middle_val == search_val:
            found = True
            return found
        elif middle_val > search_val:
            right_index = middle_index - 1
        else:
            left_index = middle_index + 1
    return found


def selection_sort(values):
    unsort_index = 0
    while unsort_index < len(values):
        lowest_value = values[unsort_index]
        start_range = range(unsort_index, len(values))
        for value_index in start_range:
            if values[value_index] < lowest_value:
                lowest_value = values[value_index]
        values.remove(lowest_value)
        values.insert(unsort_index, lowest_value)
        unsort_index += 1


def calc_area(rect):
    p1, p2 = rect.getP1(), rect.getP2()
    width = abs(p1.getX() - p2.getX())
    height = abs(p1.getY() - p2.getY())
    return width * height


def rect_sort(rectangles):
    unsort_index = 0
    while unsort_index < len(rectangles):
        lowest_value = calc_area(rectangles[unsort_index])
        start_range = range(unsort_index, len(rectangles))
        smallest_rectangle = rectangles[unsort_index]
        for value_index in start_range:
            if calc_area(rectangles[value_index]) < lowest_value:
                lowest_value = calc_area(rectangles[value_index])
                smallest_rectangle = rectangles[value_index]
        rectangles.remove(smallest_rectangle)
        rectangles.insert(unsort_index, smallest_rectangle)
        unsort_index += 1

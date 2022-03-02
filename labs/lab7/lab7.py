"""
Alex James
lab7.py
Problem: Create a weighted average of student grades.txt by reading files
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

# Open grades.txt & output


def main(file_to_open, file_to_write):
    grades_file = open(file_to_open, 'r')
    output_file = open(file_to_write, 'w')
    names_table = []
    grades_table = []
    file_lines = grades_file.readlines()
    message_table = []
    check_table = []
    for line_var in file_lines:
        line_var.strip()
        new_line_table = line_var.split(":")
        names_table.append(new_line_table[0])
        grades_table.append(new_line_table[1])
    for grade_set in grades_table:
        total_weight = 0
        grade_set.strip()
        indv_grades = grade_set.split(" ")
        grade_total = 0
        for i in range(1, (len(indv_grades)), 2):
            # odd entries are WEIGHTS, even entries are GRADES
            total_weight = eval(indv_grades[i]) + total_weight
            grade_total = (eval(indv_grades[i]) * eval(indv_grades[i + 1])) + grade_total
        if total_weight < 100:
            message = "Error: The weights are less than 100."
            check_table.append(0)
        elif total_weight > 100:
            message = "Error: The weights are greater than 100."
            check_table.append(0)
        else:
            grade_total = grade_total / 100
            message = round(grade_total, 3)
            message = str(message)
            check_table.append(1)
        message_table.append(message)
    next_student = 0
    class_average = 0
    total_students = 0
    j = 0
    final_table = []
    for message_item in message_table:
        if check_table[j] == 1:
            j = j + 1
            class_average = class_average + eval(message_item)
            student_name = names_table[next_student]
            message = student_name + "'s average: " + message_item
            next_student = next_student + 1
            total_students = total_students + 1
            print(message)
            final_table.append(message)
        else:
            j = j + 1
            student_name = names_table[next_student]
            message = student_name + "'s average: " + message_item
            next_student = next_student + 1
            print(message)
            final_table.append(message)
    class_average = class_average / total_students
    class_average = ("The class average is " + str(class_average))
    final_table.append(class_average)
    for final_message in final_table:
        print(final_message, file=output_file)
    grades_file.close()
    output_file.close()

"""
Alex James
lab13.py
Problem: Complete one of two capstone questions and then create functions in algorithms.py.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def star_find(file_to_open):
    signal_file = open(file_to_open, 'r')
    signals = signal_file.readline().split(" ")
    strong_list = []
    five_found = False
    signals_searched = 0
    for signal in signals:
        if 4000 <= eval(signal) <= 5000:
            strong_list.append(signal)
        if len(strong_list) == 5:
            five_found = True
            break
        signals_searched += 1
    return_message = "There were {} strong signals found. The strengths were: {}".format(len(strong_list), strong_list)
    if five_found:
        return_message = return_message + "\n{} signals searched before finding the 5th signal.".format(signals_searched)
    signal_file.close()
    return return_message


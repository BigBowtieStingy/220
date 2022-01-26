import math
"""
Alex James
lab1.py
Problem: Calculate different types of means for any amount of number inputs.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


"""
1: This program accepts any number of number inputs and calculates 3 different averages from the inputted numbers.
2: Inputs: The total number of numbers that should be averaged and the values of said numbers.
   Output: The RMS Average, the Harmonic Mean, and the Geometric mean.
3: First, ask user for the number of numbers th4ey want to average together. 
Secondly, ask the user for number values in a for loop that repeats based on the number gotten in step 1.
Use loop to get the sum for RMS, the denominator for the Harmonic Mean and the product for Geometric mean.
Third: Calculate the RMS value and print it.
Fourth: Calculate the Harmonic Mean value and print it.
Fifth: Calculate the Geometric Mean value and print it.
"""


def mean_calculator():
    repeat_times = eval(input("How many numbers do you want to average?"))
    # Initialize variables that will be used in the loop, geometric_mean_product must be 1
    rms_sum = 0
    harmonic_mean_denominator = 0
    geometric_mean_product = 1
    for i in range(repeat_times):
        # Ask user for each number x number of times, with x being the number they inputted in repeat_times
        requested_number = eval(input("Input a number:"))
        # Update the 3 values needed to calculate the means
        rms_sum = (requested_number ** 2) + rms_sum
        harmonic_mean_denominator = 1 / requested_number + harmonic_mean_denominator
        geometric_mean_product = geometric_mean_product * requested_number
    # Calculate & print RMS
    rms_value = math.sqrt(rms_sum / repeat_times)
    print(round(rms_value, 3), "is the RMS average.")
    # Calculate & print Harmonic Mean
    harmonic_mean_value = repeat_times / harmonic_mean_denominator
    print(round(harmonic_mean_value, 3), "is the Harmonic mean.")
    # Calculate & print Geometric Mean
    geometric_mean_value = geometric_mean_product ** (1/repeat_times)
    print(round(geometric_mean_value, 3), "is the Geometric mean.")

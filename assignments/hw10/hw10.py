"""
Name: Alex James
hw10.py
Problem: Create various programs using while loops and classes.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def fibonacci(number):
    count = 1
    fib_list = [0, 1]
    while count < number:
        fib_list.append(fib_list[count - 1] + fib_list[count])
        count += 1
    return fib_list[number]


def double_investment(principle, rate):
    cur_interest = principle
    years = 0
    while cur_interest <= (principle * 2):
        cur_interest = cur_interest * (1 + rate)
        years += 1
    return years


def syracuse(number):
    syr_list = [number]
    count = 0
    syr_num = number
    while syr_num != 1:
        if syr_num % 2 == 0:
            syr_list.append(syr_num / 2)
        else:
            syr_list.append(3 * syr_num + 1)
        count += 1
        syr_num = syr_list[count]
    return syr_list


def goldbach(number):
    possible_primes = []
    n_range = []
    count = 2
    if number / 2 != number // 2:
        return None
    while count < number:
        n_range.append(count)
        count += 1
    count = 1
    # Get every possible prime number
    while count <= number:
        is_prime = False
        is_composite = True
        possible_primes.append(count)
        # Count should only be prime numbers at this point in loop
        # This while loop waits for a prime number to be found
        while not is_prime and count <= number:
            count += 1
            try_number = 1
            while try_number < (count - 1):
                # Checks to see if the number is composite, if so it is thrown out
                # If n gets too big (greater than the starting number), the count must be prime
                try_number += 1
                is_composite = count / try_number == count // try_number
                if is_composite:
                    break
            if not is_composite:
                is_prime = True
    count = 0
    count_2 = len(possible_primes)
    while (possible_primes[count] + possible_primes[count_2 - 1]) != number:
        # Since count_2 is skipping a step each time, all combinations will eventually happen
        count += 1
        count_2 -= 2
        if count > len(possible_primes) - 1:
            count = 0
        if count_2 < 0:
            count_2 = len(possible_primes)
    return [possible_primes[count], possible_primes[count_2 - 1]]

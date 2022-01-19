"""
Alex James
lab1.py
Problem: Find the Monthly Interest of a credit card account that had some amount of money depoisted into it
during the billing cycle.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def monthly_interest():
    annual_interest_rate = eval(input("What is your annual interest rate as a percent?"))
    annual_interest_rate = annual_interest_rate / 100
    monthly_interest_rate = annual_interest_rate / 12
    # Ask for and get Annual Interest Rate as a decimal value, calculate monthly interest rate
    interest_cycle_days = eval(input("How many days is your billing cycle?"))
    previous_balance = eval(input("What was the previous balance in your account?"))
    payment_amount = eval(input("How much did you deposit into the account?"))
    payment_day = eval(input("On what day of the billing cycle did you add money into your account?"))
    # Ask for variables needed to solve for monthly interest
    balance_over_days = previous_balance * interest_cycle_days
    payment_times_days = payment_amount * (interest_cycle_days - payment_day)
    # Step 1 and Step 2 above
    avg_daily_balance = balance_over_days - payment_times_days
    avg_daily_balance = avg_daily_balance / interest_cycle_days
    # Average daily balance calculated
    monthly_interest_amount = avg_daily_balance * monthly_interest_rate
    print("$",round(monthly_interest_amount, 2), "is your monthly interest.")

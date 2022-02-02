"""
Alex James
lab3.py
Problem: Find the average number of cars that travel on any number of roads for any number of days. Then find the
average number of cars per road across all days surveyed.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def traffic():
    # Ask user for num. of roads surveyed. Loop for each road surveyed.
    num_of_roads = eval(input("How many roads were surveyed?"))
    total_cars = 0
    cars_on_road = 0
    for i in range(num_of_roads):
        cars_on_road = 0
        print("How many days was road", (i + 1), "surveyed?", end="")
        days_surveyed = eval(input())
        for j in range(days_surveyed):
            print("\tHow many cars traveled on road", i + 1, "on day", j + 1,"?", end="")
            cars_on_road = eval(input()) + cars_on_road
        total_cars = cars_on_road + total_cars
        print("The average number of cars per day on road", i + 1, "is", (cars_on_road / days_surveyed))
    print("The total number of cars on all roads is", total_cars, "cars.")
    print("The average number of cars per road is", round(total_cars / num_of_roads, 2))


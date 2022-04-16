"""
Name: Alex James
sales_person.py
Problem: Create a Salesperson class with an employee id, name, and sales.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        sale_sum = 0
        for sale in self.sales:
            sale_sum += sale
        return sale_sum

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        return self.total_sales() >= quota

    def compare_to(self, other):
        if self.total_sales() > other.total_sales():
            return 1
        if self.total_sales() < other.total_sales():
            return -1
        return 0

    def __str__(self):
        return '{}-{}: {}'.format(self.employee_id, self.name, self.total_sales())

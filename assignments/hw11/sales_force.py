"""
Name: Alex James
sales_force.py
Problem: Create a SalesForce class that contains a list of SalesPerson objects.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from sales_person import SalesPerson


class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        sales_list = open(file_name, 'r')
        count = 0
        for line in sales_list.readlines():
            line = line.replace(",", "")
            line = line.replace("\n", "")
            split_line = line.split(" ")
            current_sales_person = (SalesPerson(eval(split_line[0]), split_line[1] + " " + split_line[2]))
            for i in range(3, len(split_line)):
                current_sales_person.enter_sale(eval(split_line[i]))
            self.sales_people.append(current_sales_person)
            count += 1
        sales_list.close()

    def quota_report(self, quota):
        people_list = []
        for sales_person in self.sales_people:
            person_list = [sales_person.get_id(), sales_person.get_name(),
                           sales_person.total_sales(), sales_person.met_quota(quota)]
            people_list.append(person_list)
        return people_list

    def top_seller(self):
        people_list = []
        top_seller = self.sales_people[0]
        count = 1
        while count < len(self.sales_people):
            test_person = self.sales_people[count]
            if top_seller.total_sales() > test_person.total_sales():
                count += 1
            elif top_seller.total_sales() < test_person.total_sales():
                top_seller = test_person
                count += 1
            else:
                people_list.append(test_person)
                count += 1
        people_list.append(top_seller)
        # In the event a value ties, the code below removes values that tied lower than the highest value
        for final_person in people_list:
            if final_person.total_sales() > people_list[-1].total_sales():
                people_list.remove(final_person)
        return people_list

    def individual_sales(self, employee_id):
        for sales_person in self.sales_people:
            found = employee_id == sales_person.get_id()
            if found:
                return sales_person
        return None

    def get_sale_frequencies(self):
        sale_dict = {}
        for sales_person in self.sales_people:
            for sale in sales_person.get_sales():
                sale_dict[sale] = sale_dict.get(sale, 0) + 1
        return sale_dict

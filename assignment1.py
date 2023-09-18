"""👉 1. Create a JSON file (employee.json) containing employee information of minimum 5 employees. Each employee
information consists of Name, DOB, Height, City, State. Write a python program that reads this information from the
JSON file and saves the information into a list of objects of Employee class. Finally print the list of the Employee
objects."""

import json


class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

    def __repr__(self):
        return "This is the object of employee '" + self.name + f"' with address '{id(self)}'"


with open('employee.json', 'r') as f:
    employee_data = json.load(f)

lst = []
for emp_obj in employee_data:
    lst.append(Employee(emp_obj['name'], emp_obj['dob'], emp_obj['height'], emp_obj['city'], emp_obj['state']))

print(lst)

"""👉 2. Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file."""
state_dict = {
    "Odisha": "Bhubaneswar",
    "Karnataka": "Bengaluru",
    "Maharashtra": "Mumbai",
    "Uttarakhand": "Dehradun",
    "Uttar Pradesh": "Lucknow",
    "Telangana": "Hyderabad",
    "Tamil Nadu": "Chennai"
}

with open("state_and_their_capital.json", 'w') as f:
    f.write(json.dumps(state_dict))

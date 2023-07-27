list_1 = [100, 200, 300, 400]
print(sum(list_1))

list_2 = [500, 200, 300, 500, 100, 300, 400, 800, 400, 600, 900, 1000]
print(set(list_2))

class Dictionary:
    def __init__(self):
        self.data = {}

    def add_employee(self, name, position, salary):
        self.data[name] = (position, salary)

    def increase_salary(self, name):
        if name in self.data:
            current_position, current_salary = self.data[name]
            new_salary = current_salary * 1.5
            self.data[name] = (current_position, new_salary)
            print(f"Salary is {name} up from {current_salary} to {new_salary}.")
        else:
            print(f"Employee name '{name}' not found.")

    def display_employee_info(self, name):
        if name in self.data:
            position, salary = self.data[name]
            print(f"name: {name}, position: {position}, salary: {salary}")
        else:
            print(f"Employee name '{name}' not found.")

my_dictionary = Dictionary()

my_dictionary.add_employee("Viktor", "qa", 1000)
my_dictionary.add_employee("Mary", "pm", 1200)
my_dictionary.add_employee("Kate", "dev", 1500)

my_dictionary.increase_salary("Viktor")
my_dictionary.display_employee_info("Kate")






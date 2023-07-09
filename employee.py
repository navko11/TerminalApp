

class employee_details:
    def __init__(self, name, position, paygrade, experience):
        self.name = name
        self.position = position
        self.paygrade = paygrade
        self.experience = experience

employees = {}

name = input("Enter employee name: ")
position = input("Enter employee position: ")
paygrade = int(input("Enter employee paygrade level (0-6): "))
experience = input("Enter employee experience type (junior/medior/senior): ")


# Using employee details class
employee = employee_details(name, position, paygrade, experience)

# Add the employee to the employees dictionary
employees[name] = employee

# View added employee
for name, employee in employees.items():
    print("***** New Employee Added")
    print(f"Employee Name: {employee.name}")
    print(f"Position: {employee.position}")
    print(f"Paygrade Level: {employee.paygrade}")
    print(f"Experience: {employee.experience}")
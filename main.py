import functions

class Employee:
    def __init__(self, name, position, paygrade, experience):
        self.name = name
        self.position = position
        self.paygrade = paygrade
        self.experience = experience

def employee_details():
    name = input("Enter employee name: ")
    position = input("Enter employee position: ")
    paygrade = int(input("Enter employee paygrade level (0-6): "))
    while paygrade not in [0, 1, 2, 3, 4, 5, 6]:
        print("Invalid input")
        paygrade = int(input("Enter employee paygrade level (0-6): "))
    experience = input("Enter employee experience type (junior/medior/senior): ")
    while experience not in ["junior","medior","senior"]:
        print("Invalid input")
        experience = input("Enter employee experience type (junior/medior/senior): ")
    employee = Employee(name, position, paygrade, experience)
    return employee

current_employees = {}

# Nested loop with main menu and inner loops with sub-menus

while True:
    functions.menu()
    selection = int(input("Enter option> "))

    if selection == 1:
        functions.selection()

        selection1 = int(input("Enter option> "))

        if selection1 == 1:
            if len(current_employees) == 0:
                print("No employees to display.")
            else:
                functions.view_emp()
                for name, employee_data in current_employees.items():
                    print(f"Name: {name}")
                    print(f"Position: {employee_data['position']}")
                    print(f"Paygrade: {employee_data['paygrade']}")
                    print(f"Experience Level: {employee_data['experience']}")
                    print(functions.space)

        elif selection1 == 2:
            functions.add_emp()
            employee = employee_details()
            current_employees[employee.name] = {
                "position": employee.position,
                "paygrade": employee.paygrade,
                "experience": employee.experience
            }
            for i in range(3):
                print()
            print("***** New Employee Added *****")

        elif selection1 == 3:
            while True:
                name = input("Enter the employee name to remove: ")
                if name in current_employees:
                    del current_employees[name]
                    print(f"Employee '{name}' removed successfully")
                    break
                else:
                    print(f"Employee '{name}' does not exist")

        elif selection1 == 4:
            continue

        else:
            print("Invalid input, try again.")

    elif selection == 2:
        print("List of Pay Rates")
        # Add code for the pay rates menu

    elif selection == 3:
        print("Help Menu")
        # Add code for the help menu

    elif selection == 4:
        print("Exiting program")
        break

    else:
        print("Invalid input, try again.")

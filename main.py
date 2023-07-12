import functions
import pay

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

class SalaryLevels:
    def __init__(self):
        self.level = [45000, 60000, 75000, 90000, 105000, 120000]

    def get_salary(self, level):
        if level in range(1, len(self.level) + 1):
            return self.level[level - 1]

current_employees = {}

# Nested loop with main menu and inner loops with sub-menus

while True:
    functions.menu()
    selection = int(input("Enter option> "))

    # Entering sub-menu of "Employee Management"
    if selection == 1:
        functions.selection()

        selection1 = int(input("Enter option> "))

        # View employee section
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

        # Add employee section
        elif selection1 == 2:
            functions.add_emp()
            employee = employee_details()
            current_employees[employee.name] = {
                "position": employee.position,
                "paygrade": employee.paygrade,
                "experience": employee.experience
            }
            print()
            print("***** New Employee Added *****")
            print(functions.line)

        # Remove employee section
        # elif selection1 == 3:
        # print employee list
        #     while True:
        #         name = input("Enter the employee name to remove: ")
        #         if name in current_employees:
        #             del current_employees[name]
        #             print(f"Employee '{name}' removed successfully")
        #             break
        #         else:
        #             print(f"Employee '{name}' does not exist")

        elif selection1 == 4:
            functions.weeklypay()
            for i, worker in enumerate(current_employees.keys()):
                print(f"{i+1}. {worker}")

            employee_index = int(input("Select employee #: "))

            employee_list = list(current_employees.keys())
    
            if employee_index in range(1, len(employee_list) + 1):
                selected_employee = employee_list[employee_index - 1]
                print(f"You selected: {selected_employee}")
            else:
                print("Invalid employee selection.")

            


        # elif selection1 == 5:
        #     continue

        # else:
        #     print("Invalid input, try again.")

    # Entering sub-menu of "List of Pay Rates"
    elif selection == 2:
        print("List of Paygrades")
        print(pay.paygrade_list())

    elif selection == 3:
        print("Help Menu")
        # Add code for the help menu

    elif selection == 4:
        print("Exiting program")
        break

    else:
        print("Invalid input, try again.")

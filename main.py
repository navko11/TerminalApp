import functions
import pay

class Employee:
    def __init__(self, name, position, paygrade):
        self.name = name
        self.position = position
        self.paygrade = paygrade

def employee_details():
    name = input("Enter employee name: ").title()
    position = input("Enter employee position: ").title()
    paygrade = int(input("Enter employee paygrade level (0-6): "))
    while paygrade not in [0, 1, 2, 3, 4, 5, 6]:
        print("Invalid input")
    employee = Employee(name, position, paygrade)
    return employee

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
                    print(functions.space)

        # Add employee section
        elif selection1 == 2:
            functions.add_emp()
            employee = employee_details()
            current_employees[employee.name] = {
                "position": employee.position,
                "paygrade": employee.paygrade,
            }
            print()
            print("***** New Employee Added *****")
            print(functions.line)

        # Remove employee section
        elif selection1 == 3:
            for i, worker in enumerate(current_employees.keys()):
                print(f"{i+1}. {worker}")

            employee_index = int(input("Input employee list number to remove: "))
            employee_list = list(current_employees.keys())
    
            if employee_index in range(1, len(employee_list) + 1):
                selected_employee = employee_list[employee_index - 1]
                del current_employees[selected_employee]
                print(f"***** {selected_employee} has been removed.*****")
            else:
                print("Invalid input.")

        elif selection1 == 4:
            functions.weeklypay()
            for i, worker in enumerate(current_employees.keys()):
                print(f"{i+1}. {worker}")

            employee_index = int(input("Select employee #: "))

            employee_list = list(current_employees.keys())
    
            if employee_index in range(1, len(employee_list) + 1):
                selected_employee = employee_list[employee_index - 1]
                int(input(f"Input weekly hours worked for {selected_employee}: "))
                

            else:
                print("Invalid employee selection.")

            


        elif selection1 == 5:
            continue

        else:
            print("Invalid input, try again.")

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

import functions
import pay
from art import *
from colorama import init, Fore, Style

init()

tprint("Payroll App")

class Employee:
    def __init__(self, name, position, paygrade):
        self.name = name
        self.position = position
        self.paygrade = paygrade

def employee_details():
    name = input("Enter employee name: ").title()
    position = input("Enter employee position: ").title()
    while True:
        paygrade = int(input("Enter employee paygrade level (1-6): "))
        if paygrade in [1, 2, 3, 4, 5, 6]:
            break
        else:
            print("Invalid input")
    employee = Employee(name, position, paygrade)
    return employee

def calculate_hourly_rate(yearly_salary, hours_per_week=40, weeks_per_year=52):
    return yearly_salary / (hours_per_week * weeks_per_year)

salary1 = 45000
salary2 = 60000
salary3 = 75000
salary4 = 90000
salary5 = 105000
salary6 = 120000

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
                print(functions.space)
                print(Fore.LIGHTRED_EX +"*****No employees to display.*****"+ Style.RESET_ALL)
                print(functions.space)
                input(Fore.LIGHTYELLOW_EX + "Press any key to return"+ Style.RESET_ALL)
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
            print(functions.space)
            print(Fore.GREEN + "***** New Employee Added *****"+ Style.RESET_ALL)
            print(functions.space)

        # Remove employee section
        elif selection1 == 3:
            functions.removeemp()
            if len(current_employees) == 0:
                print(Fore.RED + "***** No employees to remove. *****" + Style.RESET_ALL)
                print(functions.space)
                input(Fore.LIGHTYELLOW_EX + "Press any key to return" + Style.RESET_ALL)
            else:
                while True:
                    for i, worker in enumerate(current_employees.keys()):
                        print(f"{i+1}. {worker}")
                        print(functions.space)

                    employee_list = list(current_employees.keys())
                    employee_index = int(input("Input employee list number to remove or 0 to return: "))

                    if employee_index in range(1, len(employee_list) + 1):
                        selected_employee = employee_list[employee_index - 1]
                        del current_employees[selected_employee]
                        print(functions.space)
                        print(Fore.RED + f"***** {selected_employee} has been removed. *****" + Style.RESET_ALL)
                        print(functions.space)
                        break
                    elif employee_index == 0:
                        break
                    else:
                        print(functions.space)
                        print(Fore.RED +"Invalid input, Try again"+ Style.RESET_ALL)
                        print(functions.space)

        elif selection1 == 4:
            functions.weeklypay()
            if len(current_employees) == 0:
                print(Fore.RED + "*****No employees to select.*****"+ Style.RESET_ALL)
                print(functions.space)
                input(Fore.LIGHTYELLOW_EX + "Press any key to return"+ Style.RESET_ALL)
            else:
                for i, worker in enumerate(current_employees.keys()):
                    print(f"{i+1}. {worker}")
                    print(functions.space)

                employee_index = int(input("Select employee #: "))
                employee_list = list(current_employees.keys())

                if employee_index in range(1, len(employee_list) + 1):
                    selected_employee = employee_list[employee_index - 1]
                    hours_worked = int(input(f"Input weekly hours worked for {selected_employee}: "))
                    print(functions.space)

                    paygrade = current_employees[selected_employee]['paygrade']

                    if paygrade == 1:
                        level1 = calculate_hourly_rate(salary1)
                        weekly_pay = level1 * hours_worked

                    elif paygrade == 2:
                        level2 = calculate_hourly_rate(salary2)
                        weekly_pay = level2 * hours_worked

                    elif paygrade == 3:
                        level3 = calculate_hourly_rate(salary3)
                        weekly_pay = level3 * hours_worked

                    elif paygrade == 4:
                        level4 = calculate_hourly_rate(salary4)
                        weekly_pay = level4 * hours_worked

                    elif paygrade == 5:
                        level5 = calculate_hourly_rate(salary5)
                        weekly_pay = level5 * hours_worked

                    elif paygrade == 6:
                        level6 = calculate_hourly_rate(salary6)
                        weekly_pay = level6 * hours_worked

                    print(f"Employee: {selected_employee}")
                    print(f"Position: {current_employees[selected_employee]['position']}")
                    print(f"Paygrade: {paygrade}")
                    print(f"Hours worked: {hours_worked}")
                    print(f"Gross Weekly pay: ${weekly_pay:.2f}")
                    print(functions.space)

                else:
                    print("Invalid employee selection.")

        elif selection1 == 5:
            continue

        else:
            print("Invalid input, try again.")

    # Entering sub-menu of "List of Pay Rates"
    elif selection == 2:
        functions.viewpaygrade()
        print(Fore.LIGHTMAGENTA_EX + "*Note - Figures below are in gross pay*" + Style.RESET_ALL)
        print(functions.space)
        print(pay.paygrade_list())
        input(Fore.LIGHTYELLOW_EX + "Press any key to return"+ Style.RESET_ALL)

    elif selection == 3:
        print("Exiting program")
        break

    else:
        print(functions.space)     
        print(Fore.RED +"Invalid input, try again."+ Style.RESET_ALL)
        print(functions.space)


import functions
import test
import pay

class employee_details:
    def __init__(self, name, position, paygrade, experience):
        self.name = name
        self.position = position
        self.paygrade = paygrade
        self.experience = experience

# # View added employee
# for name, employee in employees.items():
#     print("***** New Employee Added")
#     print(f"Employee Name: {employee.name}")
#     print(f"Position: {employee.position}")
#     print(f"Paygrade Level: {employee.paygrade}")
#     print(f"Experience: {employee.experience}")

# # Outer menu loop




while True:
    functions.menu()
  
    
    selection = int(input("Enter option> "))

    
    # Inner menu loop
    if selection == 1:
        print("1. List of Employees")
        print("2. Add Employee")
        print("3. Remove Employee")
        print("4. Back")

        selection1 = int(input("Enter option> "))
        
        while True:
            if selection1 == 2:
                employees = {}

                name = input("Enter employee name: ")
                position = input("Enter employee position: ")
                paygrade = int(input("Enter employee paygrade level (0-6): "))
                experience = input("Enter employee experience type (junior/medior/senior): ")
                employee = employee_details(name, position, paygrade, experience)
                employees[name] = employee # Add the employee to the employees dictionary
                for name, employee in employees.items():
                    print("***** New Employee Added")
                    print(f"Employee Name: {employee.name}")
                    print(f"Position: {employee.position}")
                    print(f"Paygrade Level: {employee.paygrade}")
                    print(f"Experience: {employee.experience}")


    # elif selection == 2:
    #     print("List of Pay Rates"), # Add code for the pay rates menu
        
    # elif selection == 3:
    #     print("Help Menu"), # Add code for the help menu

    # elif selection == 4:
    #     print("Exiting program")
    #     break
    
    # else:
    #     print("Invalid input, try again.")
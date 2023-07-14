# make minimum 6 functions
line = ("-" * 64)
double_line = ("=" * 64)
space = (" " * 64)
# Menu function


def menu():
    print(double_line)
    print("Main Menu")
    print(double_line)
    print("1. Employee Management")
    print("2. List of Paygrades")
    print("3. Help")
    print("4. Exit Program")
    print(line)

def selection():
    print(space)
    print(double_line)
    print("Current Employees")
    print(double_line)
    print("1. View Employees")
    print("2. Add Employee")
    print("3. Remove Employee")
    print("4. Employee hours worked (weekly)")
    print("5. Back")
    print(line)

def add_emp():
    print(space)
    print(double_line)
    print("Add Employee")
    print(double_line)

def view_emp():
    print(space)
    print(double_line)
    print("List of Employees")
    print(double_line)
    print(space)

def weeklypay():
    print(space)
    print(double_line)
    print("Employee weekly payslip")
    print(double_line)
    print(space)

def weekly_hours():
    int(input("Input weekly hours employee has worked: "))

    
# Make a calculation function


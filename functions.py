from colorama import init, Fore, Style
init()

# Borders and spacing
line = ("-" * 64)
double_line = ("=" * 64)
space = (" " * 64)


# Menu function
def menu():
    print(double_line)
    print(Fore.LIGHTCYAN_EX + "Main Menu" + Style.RESET_ALL)
    print(double_line)
    print("1. Employee Management")
    print("2. List of Paygrades")
    print("3. Exit Program")
    print(line)

def selection():
    print(space)
    print(double_line)
    print(Fore.LIGHTGREEN_EX + "Employee Management" + Style.RESET_ALL)
    print(double_line)
    print("1. View Employees")
    print("2. Add Employee")
    print("3. Remove Employee")
    print("4. Employee hours worked (weekly)")
    print("5. Back")
    print(line)


# all menu and sub-menu borders and spacing below

def add_emp():
    print(space)
    print(double_line)
    print(Fore.LIGHTMAGENTA_EX +"Add Employee"+ Style.RESET_ALL)
    print(double_line)
    print(space)

def view_emp():
    print(space)
    print(double_line)
    print(Fore.LIGHTGREEN_EX + "List of Employees"+ Style.RESET_ALL)
    print(double_line)
    print(space)

def weeklypay():
    print(space)
    print(double_line)
    print(Fore.CYAN +"Employee weekly payslip"+ Style.RESET_ALL)
    print(double_line)
    print(space)

def viewpaygrade():
    print(space)
    print(double_line)
    print(Fore.LIGHTMAGENTA_EX + "List of Paygrades" + Style.RESET_ALL)
    print(double_line)
    print(space)

def removeemp():
    print(space)
    print(double_line)
    print(Fore.LIGHTRED_EX+ "Remove Employee" + Style.RESET_ALL)
    print(double_line)
    print(space)


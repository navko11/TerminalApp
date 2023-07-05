import draft
#Main menu


def main():
    print("1. View employees")
    print("2. View payrates")
    print("3. Help")
    print("4. Exit program")



print("Welcome to Payroll")
print("------------------")
main()

selection = int(input("Enter option> "))

while selection != 4:
    if selection == 1:
        print(draft.employees)
    elif selection == 2:
        print("List of payrates")
    elif selection == 3:
        print("Help list")
    elif selection == 4:
        print("Exiting program")
    else:
        print("Invalid input, try again.")
    
    selection = int(input("Enter option> "))
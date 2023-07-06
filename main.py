import employee

line1 = "-" * 50
line2 = "*" * 50
space = " " * 50

# Outer menu loop
while True:
    print(line1)
    print("Main Menu")
    print(line1)
    print(space)
    print("1. List of Employees")
    print("2. List of Pay Rates")
    print("3. Help")
    print("4. Exit Program")
    print(space)
    print(line2)
    print(space)
    
    selection = int(input("Enter option> "))
    print(line1)
    
    # Inner menu loop
    if selection == 1:
        print("List of Employees")
        print(line1)
        print(space)
        1
        while True:
            for key, value in employee.employees.items():
                print(key, value)

            print(space)
            print("1. View employee")
            print("2. Go back to the main menu")
            print(space)
            nested_selection = int(input("Enter option> "))
            
            if nested_selection == 2:
                break
            elif nested_selection == 1:
                int(input("Enter option> "))
            else:
                print("Invalid input, try again.")
    
    elif selection == 2:
        print("List of Pay Rates")
        print("----------------")
        # Add code for the pay rates menu
        
    elif selection == 3:
        print("Help Menu")
        print("---------")
        # Add code for the help menu
        
    elif selection == 4:
        print("Exiting program")
        break
    
    else:
        print("Invalid input, try again.")

T1A3 - Terminal Application - Mark Navarro
https://github.com/navko11/TerminalApp/tree/master

The project that I have decided to make is a replication of a simple payroll system.
The system will allow you to view/add/remove employees and input basic information of employees.
After all the inputs are declared with values, the result of the payslip of the employee will be displayed.

Python version 3.11.4

As long as the python version is above 3.7 the app should run with no problem
I had to input these commands in order to open virtual environment in my Windows system, it may be different for linux/mac users.
1. python -m venv tutorial-env              
2. Set-ExecutionPolicy Unrestricted -Scope Process
3. tutorial-env\Scripts\activate
4. python main.py

Packages used taken from https://pypi.org/:
- pip install art
- pip install colorama              

Features of the app:

1. Adding employee information

When in add menu option, user will be prompted to input new employee details.
![Alt text](../appscreenshots/addemp.jpg)

When completed, a notice will be output to confirm addition of employee .
![Alt text](../appscreenshots/addemp1.jpg)

Employee class and function is created to define the information inputted by the user.
While loop is used to handle the error if invalid input is made in that input.
![Alt text](../appscreenshots/classemployee(add1).jpg)

inputs are transferred as a key and value and is stored to a dictionary.
functions are included and imported from other modules.
![Alt text](../appscreenshots/classemployee(add2).jpg)

If input is not 1-6 error message will be thrown and user can attempt to input valid number.
![Alt text](../appscreenshots/erroraddemp.jpg)

2. Removing employee



3. Displaying employees payslip with defined inputs






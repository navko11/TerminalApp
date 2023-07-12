#how many hours worked
#deductions

"salary to hourly rate conversion"
 
salary1 = 45000
salary2 = 60000
salary3 = 75000
salary4 = 90000
salary5 = 105000
salary6 = 120000

level = [salary1, salary2, salary3, salary4, salary5, salary6]

# Display the menu
# print("Pay Levels:")
# for i, salary in enumerate(level):
#     print(f"{i+1}. ${salary}/pa")

# Prompt for level selection1
selected_level = int(input("Select a pay level (1-6): "))

if selected_level in range(1, 7):
    annual_salary = level[selected_level - 1]
    hours_per_week = 40
    weeks_per_year = 52

    hourly_rate = annual_salary / (hours_per_week * weeks_per_year)

    print(f"The hourly rate for pay level {selected_level} is ${hourly_rate:.2f}")
else:
    print("Invalid pay level selected.")

def weekly_hours():
    int(input("Input weekly hours employee has worked: "))

# Get hourly rate from yearly salary
# Calculate hourly rate with hours worked
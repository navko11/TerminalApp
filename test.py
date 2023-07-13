

# Get hourly rate from yearly salary
# Calculate hourly rate with hours worked


class SalaryLevels:
    def __init__(self):
        self.levels = [45000, 60000, 75000, 90000, 105000, 120000]

    def get_salary(self, level):
        if level in range(1, len(self.levels) + 1):
            return self.levels[level - 1]

# Create an instance of the SalaryLevels class
salary_levels = SalaryLevels()

salary_level = 1
weekly_hours = int(input("Input weekly hours worked: "))

salary = salary_levels.get_salary(salary_level)
if salary is not None:
    hourly_rate = salary / (weekly_hours * 52)
    print(f"Weekly payslip for Salary Level {salary_level}:")
    print(f"Hourly Rate: ${hourly_rate:.2f}")
    print(f"Weekly Salary: ${salary/52:.2f}")
else:
    print("Invalid salary level")
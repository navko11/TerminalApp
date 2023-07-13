def paygrade_list():
    salary1 = 45000
    salary2 = 60000
    salary3 = 75000
    salary4 = 90000
    salary5 = 105000
    salary6 = 120000

    print(f"Salary level 1 = ${salary1:,}/pa")
    print(f"Salary level 2 = ${salary2:,}/pa")
    print(f"Salary level 3 = ${salary3:,}/pa")
    print(f"Salary level 4 = ${salary4:,}/pa")
    print(f"Salary level 5 = ${salary5:,}/pa")
    print(f"Salary level 6 = ${salary6:,}/pa")

    class SalaryLevels:
        def __init__(self):
            self.level = [45000, 60000, 75000, 90000, 105000, 120000]

        def get_salary(self, level):
            if level in range(1, len(self.level) + 1):
                return self.level[level - 1]
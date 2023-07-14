def paygrade_list():
    salary1 = 45000
    salary2 = 60000
    salary3 = 75000
    salary4 = 90000
    salary5 = 105000
    salary6 = 120000

    result = ""
    result += f"Salary level 1 = ${salary1:,}/pa\n"
    result += f"Salary level 2 = ${salary2:,}/pa\n"
    result += f"Salary level 3 = ${salary3:,}/pa\n"
    result += f"Salary level 4 = ${salary4:,}/pa\n"
    result += f"Salary level 5 = ${salary5:,}/pa\n"
    result += f"Salary level 6 = ${salary6:,}/pa\n"

    return result
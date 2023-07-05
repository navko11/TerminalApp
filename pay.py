serviceyears = list(range(30))

paybase = {
    'level1' : '45000',
    'level2' : '60000',
    'level3' : '75000',
    'level4' : '90000',
    'level5' : '105000',
    'level6' : '120000',
}

payincrease = {
    'junior' : '0.03',
    'medior' : '0.0275',
    'senior' : '0.0225'
}

if serviceyears <= list[3]:
    payincrease['junior'] = True
elif serviceyears == list[4] and serviceyears <= list[9]:
    payincrease['medior'] = True
else:
    payincrease['senior'] = True

employees = {
    'worker1': {
        'name': 'Mark',
        'age': '31',
        'position': '???',
        'salary': 'level2',
        'yearsworked' : '4'
    },
    'worker2': {
        'name': 'John',
        'age': '23',
        'position': '???',
        'salary': 'level1',
        'yearsworked' : '1'
    },
        'worker3': {
        'name': 'Steve',
        'age': '40',
        'position': '???',
        'salary': 'level4',
        'yearsworked' : '15'
    },
}


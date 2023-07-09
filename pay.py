

level1 = 45000
level2 = 60000
level3 = 75000
level4 = 90000
level5 = 105000
level6 = 120000

junior = 0.03 # 0-2 years
medior = 0.0275 # 2-3 years
senior = 0.025 # 3+ years

paygrade = [level1, level2, level3, level4, level5, level6]
experience = [junior, medior, senior]


print(paygrade[0] * experience[2])
print(paygrade[1] + (paygrade[1] * experience[0]))
"""Case-study #2 Прогрессивное налогообложение
Developers:
Sychov A., Virt A., Ostanina K.

"""
import local

print(local.RU_INPUT_UR_FAMILY_CATEGORY)
print("(1) " + local.RU_ONLY_ONE)
print("(2) " + local.RU_PARENTS)
print("(3) " + local.RU_SINGLE_PARENT)
status = int(input())

"""print(local.RU_INPUT_UR_MONTHLY_IN_DOLLARS)
salary = int(input()) * 12
"""
names_months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
                'november', 'december']
annual_salary = 0
for month in range(12):
    print("Ваша зарплата в", names_months[month], "(В долларах):")
    salary = float(input())
    annual_salary += salary
    
if status == 1:
    if 0 < annual_salary <= 9075:
        tax = 0.1*annual_salary
    elif annual_salary <= 36900:
        tax = 907.5 + (annual_salary-9075)*0.15
    elif annual_salary <= 89350:
        tax = 5081.25 + (annual_salary-36900)*0.25
    elif annual_salary <= 186350:
        tax = 18193.75 + (annual_salary-89350)*0.28
    elif annual_salary <= 405100:
        tax = 45353.75 + (annual_salary-186350)*0.33
    elif annual_salary <= 406750:
        tax = 117541.25 + (annual_salary-405100)*0.35
    elif annual_salary > 406750:
        tax = 118118.75 + (annual_salary-406750)*0.396
elif status == 2:

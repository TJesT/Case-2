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

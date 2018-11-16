"""Case-study #2 Прогрессивное налогообложение
Developers:
Sychov A., Virt A., Ostanina K.

"""
import local

NAME_OF_MONTHS = [
  local.RU_MONTH_JANUARY, 
  local.RU_MONTH_FEBRUARY, 
  local.RU_MONTH_MARCH,
  local.RU_MONTH_APRIL,
  local.RU_MONTH_MAY, 
  local.RU_MONTH_JUNE, 
  local.RU_MONTH_JULY, 
  local.RU_MONTH_AUGUST, 
  local.RU_MONTH_SEPTEMBER, 
  local.RU_MONTH_OCTOBER, 
  local.RU_MONTH_NOVEMBER, 
  local.RU_MONTH_DECEMBER
]

print(local.RU_INPUT_UR_FAMILY_CATEGORY)
print("(1) " + local.RU_ONLY_ONE)
print("(2) " + local.RU_PARENTS)
print("(3) " + local.RU_SINGLE_PARENT)
status = int(input())

annual_salary = 0
for month in NAME_OF_MONTHS:
    print(local.RU_INPUT_UR_TAX, month, local.RU_IN_DOLLARS)
    salary = float(input())
    annual_salary += salary

"""Case-study #2 Прогрессивное налогообложение
Developers:
Sychov A., Virt A., Ostanina K.

"""
import Local

NAME_OF_MONTHS = [
    Local.RU_MONTH_JANUARY,
    Local.RU_MONTH_FEBRUARY,
    Local.RU_MONTH_MARCH,
    Local.RU_MONTH_APRIL,
    Local.RU_MONTH_MAY,
    Local.RU_MONTH_JUNE,
    Local.RU_MONTH_JULY,
    Local.RU_MONTH_AUGUST,
    Local.RU_MONTH_SEPTEMBER,
    Local.RU_MONTH_OCTOBER,
    Local.RU_MONTH_NOVEMBER,
    Local.RU_MONTH_DECEMBER
] 

print(Local.RU_INPUT_UR_FAMILY_CATEGORY)
print("(1) " + Local.RU_ONLY_ONE)
print("(2) " + Local.RU_PARENTS)
print("(3) " + Local.RU_SINGLE_PARENT)
status = int(input())

annual_salary = 0
for month in NAME_OF_MONTHS:
    print(Local.RU_INPUT_UR_TAX, month, Local.RU_IN_DOLLARS)
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
      if 0 < annual_salary <= 18150:
        tax = annual_salary*0.1
    elif annual_salary <= 73800:
        tax = 1815 + (annual_salary-18150)*0.15
    elif annual_salary <= 148850:
        tax = 10162.5 + (annual_salary-73800)*0.25
    elif annual_salary <= 226850:
        tax = 28925 + (annual_salary-148850)*0.28
    elif annual_salary <= 405100 :
        tax = 50765 + (annual_salary-226850)*0.33
    elif annual_salary <= 457600:
        tax = 109587.5 + (annual_salary-405100)*0.35
    elif annual_salary > 457600:
        tax = 127962.5 + (annual_salary-457600)*0.396
elif status == 3:
  if 0 < annual_salary <= 18150:
        tax = annual_salary*0.1
  elif annual_salary <= 73800:
        tax = 1815 + (annual_salary-18150)*0.15
  elif annual_salary <= 148850:
      tax = 10162.5 + (annual_salary-9075)*0.25
  elif annual_salary <= 226850:
      tax = 28925 + (annual_salary-9075)*0.28
  elif annual_salary <= 405100 :
      tax = 50765 + (annual_salary-9075)*0.33
  elif annual_salary <= 457600:
      tax = 109587.5 + (annual_salary-9075)*0.35
  elif annual_salary > 457600:
      tax = 127962.5 + (annual_salary-9075)*0.396
 print(tax)

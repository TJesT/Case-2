"""Case-study #2 Прогрессивное налогообложение
Developers:
Sychov A., Virt A., Ostanina K.

"""
import Local

FIRST = [406750, 405100, 186350, 89350, 36900, 9075, 0]
SECOND = [457600, 405100, 226850, 148850, 73800, 18150, 0]
THIRD = [432200, 405100, 206600, 127550, 49400, 12950, 0]
TAX = [0.396, 0.35, 0.33, 0.28, 0.25, 0.15, 0.1]


print(Local.RU_INPUT_UR_FAMILY_CATEGORY)
print("(1) " + Local.RU_ONLY_ONE)
print("(2) " + Local.RU_PARENTS)
print("(3) " + Local.RU_SINGLE_PARENT)
status = int(input())


annual_salary = 0
for month in Local.RU_NAME_OF_MONTHS:
    print(Local.RU_INPUT_UR_TAX, month, Local.RU_IN_DOLLARS)
    salary = float(input())
    annual_salary += salary
    
def scr():
    for point in range(7):
        if status == 1:
            if annual_salary >= FIRST[point]:
                finaltax = (annual_salary - FIRST[point]) * TAX[point]
                while FIRST[point] != 0:
                    point1 = point + 1
                    finaltax = finaltax + (FIRST[point] - FIRST[point1]) * TAX[point1]
                    point += 1
                return round(finaltax, 2)
        elif status == 2:
            if annual_salary >= second[point]:
                finaltax = (annual_salary - SECOND[point]) * TAX[point]
                while SECOND[point] != 0:
                    point1 = point + 1
                    finaltax = finaltax + (SECOND[point] - SECOND[point1]) * TAX[point1]
                    point += 1
                return round(finaltax, 2)
        else:
            if annual_salary >= THIRD[point]:
                finaltax = (annual_salary - THIRD[point])*TAX[point]
                while THIRD[point] != 0:
                    point1 = point+1
                    finaltax = finaltax + (THIRD[point] - THIRD[point1])*TAX[point1]
                    point += 1
                return round(finaltax, 2)
      
    
print(Local.RU_TOTALS, scr())

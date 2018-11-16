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
    
first = [406750, 405100, 186350, 89350, 36900, 9075, 0]
second = [457600, 405100, 226850, 148850, 73800, 18150, 0]
third = [432200, 405100, 206600, 127550, 49400, 12950, 0]
tax = [0.396, 0.35, 0.33, 0.28, 0.25, 0.15, 0.1]
def scr():
    for point in range(7):
        if status == 1:
            if annual_salary >= first[point]:
                finaltax = (annual_salary - first[point]) * tax[point]
                while first[point] != 0:
                    point1 = point + 1
                    finaltax = finaltax + (first[point] - first[point1]) * tax[point1]
                    point += 1
                return round(finaltax, 2)
        elif status == 2:
            if annual_salary >= second[point]:
                finaltax = (annual_salary - second[point]) * tax[point]
                while second[point] != 0:
                    point1 = point + 1
                    finaltax = finaltax + (second[point] - second[point1]) * tax[point1]
                    point += 1
                return round(finaltax, 2)
        elif status == 3:
            if annual_salary >= third[point]:
                finaltax = (annual_salary - third[point])*tax[point]
                while third[point] != 0:
                    point1 = point+1
                    finaltax = finaltax + (third[point] - third[point1])*tax[point1]
                    point += 1
                return round(finaltax, 2)
print(scr())

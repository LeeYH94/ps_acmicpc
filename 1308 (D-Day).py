def calculate(year, month, date):
    year_day = (year - 1) * 365 + (year - 1) // 400 + (year - 1) // 4 - (year - 1) // 100
    month_day = 0
    if month == 2:
        month_day = 31

    if (year % 400 == 0) or ((year % 4 == 0) and not (year % 100 == 0)):
        if 3 <= month <= 7:
            month_day = (month - 1) * 30 + (month - 2) // 2
        elif 8 <= month <= 12:
            month_day = (month - 1) * 30 + (month - 1) // 2

    else:
        if 3 <= month <= 7:
            month_day = (month - 1) * 30 + (month - 2) // 2 - 1
        elif 8 <= month <= 12:
            month_day = (month - 1) * 30 + (month - 1) // 2 - 1

    day = year_day + month_day + date
    return day


lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
day = calculate(lst2[0], lst2[1], lst2[2]) - calculate(lst1[0], lst1[1], lst1[2])
if lst2[0] - lst1[0] >= 1000 and lst2[1] - lst1[1] >= 0 and lst2[2] - lst1[2] >= 0:
    print("gg")
else:
    print("D-", end = "")
    print(day)
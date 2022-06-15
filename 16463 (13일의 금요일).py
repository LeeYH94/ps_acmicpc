def calculate(date, month, year):
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
    if day % 7 == 5:
        global cnt
        cnt += 1


n = int(input())
cnt = 0
for i in range(2019, n+1):
    for j in range(1, 13):
        calculate(13, j, i)
print(cnt)
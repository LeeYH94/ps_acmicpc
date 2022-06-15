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

    day_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    return day_of_week[day % 7]


a, b = map(int, input().split())
print(calculate(2009, b, a))
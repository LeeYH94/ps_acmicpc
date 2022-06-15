x, y = input().split()
x = int(x)
y = int(y)

date = 0
lst = [0, 31, 28, 31, 30, 31, 30, 31, 31 , 30, 31, 30]

for i in range(0, x):
    date += lst[i]
    
date += y

day_of_week = ['SUN','MON','TUE', 'WED', 'THU', 'FRI', 'SAT']

print(day_of_week[date % 7])

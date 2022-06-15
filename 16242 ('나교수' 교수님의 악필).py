from math import ceil
n = int(input())
total = 0
for _ in range(n):
    s = input()
    temp = ''
    for i in s:
        if i == '0' or i == '6' or i == '9':
            temp += '9'
        else:
            temp += i
    if int(temp) > 100:
        temp = '100'
    total += int(temp)
if total/n - total//n >= 0.5:
    print(total//n + 1)
else:
    print(total//n)
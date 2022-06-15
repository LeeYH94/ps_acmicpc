n = int(input())
lst = input().split()

maximum = 0
result = 0

for i in lst:
    result += int(i)
    if int(i) > maximum:
        maximum = int(i)

print((result * 100 / maximum) / n)

lst = list(map(int, input().split()))

result = 0
for i in range(len(lst)):
    result += (lst[i] * lst[i])
print(result % 10)

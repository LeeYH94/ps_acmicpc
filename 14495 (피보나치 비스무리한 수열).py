lst = [0] * 117
n = int(input())
for i in range(1, 4):
    lst[i] = 1
if n >= 4:
    for i in range(4, n + 1):
        lst[i] = lst[i - 1] + lst[i - 3]
print(lst[n])

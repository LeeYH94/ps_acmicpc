a, b, c = map(int, input().split())
lst = [0] * 101
ans = 0
for i in range(3):
    n, m = map(int, input().split())
    for j in range(n, m):
        lst[j] += 1
for i in lst:
    if i == 1:
        ans = ans + a
    elif i == 2:
        ans = ans + b * 2
    elif i == 3:
        ans = ans + c * 3
print(ans)
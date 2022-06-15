from math import sqrt
n = int(input())
ans = 0
for i in range(int(sqrt(2 * n))+1):
    if i * (i + 1) // 2 <= n:
        ans = i
print(ans)
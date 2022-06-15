from math import sqrt

a = int(input())
b = int(input())
lst = []
ans = 0
for i in range(a, b+1):
    if sqrt(i) == int(sqrt(i)):
        lst.append(i)
        ans += i
if len(lst) == 0:
    print(-1)
else:
    print(ans)
    print(lst[0])
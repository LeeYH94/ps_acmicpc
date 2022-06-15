lst = []
ans = 0
for i in range(7):
    n = int(input())
    if n % 2 != 0:
        lst.append(n)
        ans += n
if len(lst) == 0:
    print(-1)
else:
    lst = sorted(lst)
    print(ans)
    print(lst[0])

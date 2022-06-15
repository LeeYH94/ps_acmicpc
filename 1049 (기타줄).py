import sys
n, m = map(int, sys.stdin.readline().split())
lst_1 = [0 for _ in range(m)]
lst_2 = [0 for _ in range(m)]
ans = 0

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    lst_1[i] = a
    lst_2[i] = b
bundle = sorted(lst_1)[0]
piece = sorted(lst_2)[0]

while True:
    if n < 6:
        if bundle < piece * n:
            ans += bundle
            break
        else:
            ans += piece * n
            break
    else:
        if bundle < piece * 6:
            ans += (n // 6) * bundle
            n %= 6
        else:
            ans += piece * n
            break
print(ans)
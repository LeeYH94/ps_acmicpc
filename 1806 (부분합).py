import sys
n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

e = 0
interval = 0
min_len = 10**15

for s in range(n):
    while interval < m and e < n:
        interval += lst[e]
        e += 1

    if interval >= m:
        min_len = min(min_len, e-s)
    interval -= lst[s]

print(min_len if min_len != 10**15 else 0)
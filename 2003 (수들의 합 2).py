import sys
n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
e = 0
cnt = 0
interval = 0

for s in range(n):
    while interval < m and e < n:
        interval += lst[e]
        e += 1
    if interval == m:
        cnt += 1
    interval -= lst[s]
print(cnt)

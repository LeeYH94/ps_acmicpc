import sys
n, m = map(int, sys.stdin.readline().split())
lst = [0 for _ in range(n)]
for i in range(n):
    lst[i] = int(sys.stdin.readline().strip())

lst.sort()
ans = 10**15
e, s = 0, 0
while s < n and e < n:
    interval = lst[e] - lst[s]
    if interval < m:
        e += 1
        continue
    elif m == interval:
        print(m)
        exit(0)
    s += 1
    ans = min(ans, interval)
print(ans)
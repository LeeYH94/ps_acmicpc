import sys
n = int(sys.stdin.readline().strip())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()

cnt = 0
if n <= 2:
    print(0)
    exit(0)

for i in range(n):
    s = 0
    e = n-1
    while s < e:
        if s == i:
            s += 1
        if e == i:
            e -= 1
        if s >= e:
            break
        good = lst[s] + lst[e]
        if lst[i] < good:
            e -= 1
        elif lst[i] > good:
            s += 1
        else:
            cnt += 1
            break
print(cnt)
import sys

for _ in range(int(sys.stdin.readline().strip())):
    n = int(sys.stdin.readline().strip())
    lst = [0 for _ in range(n)]
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        lst[a-1] = b

    temp = lst[0]
    cnt = 1

    for i in range(1, n):
        if lst[i] < temp:
            temp = lst[i]
            cnt += 1
    print(cnt)
import sys
n = int(sys.stdin.readline())
lst = [[] for _ in range(n)]
for i in range(n):
    s = sys.stdin.readline().strip()
    for j in s:
        if j == ".":
            lst[i].append(1)
        else:
            lst[i].append(0)

row = 0
col = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if lst[i][j]:
            cnt += 1
            if j == n-1 and cnt >= 2:
                row += 1
        elif not lst[i][j]:
            if cnt >= 2:
                row += 1
            cnt = 0

for i in range(n):
    cnt = 0
    for j in range(n):
        if lst[j][i]:
            cnt += 1
            if j == n-1 and cnt >= 2:
                col += 1
        elif not lst[j][i]:
            if cnt >= 2:
                col += 1
            cnt = 0

print("{} {}".format(row, col))
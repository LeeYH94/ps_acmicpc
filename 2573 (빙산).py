import sys
sys.setrecursionlimit(1000000)
row, col = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]
move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
freeze = [[0 for _ in range(col)] for _ in range(row)]
for i in range(row):
    for j in range(col):
        if graph[i][j] > 0:
            freeze[i][j] = 1


def DFS(r, c, visited):
    visited[r][c] = 1
    for k in move:
        new_row = r + k[0]
        new_col = c + k[1]
        if not visited[new_row][new_col] and graph[new_row][new_col] > 0:
            DFS(new_row, new_col, visited)


def check_split():
    visited = [[0 for _ in range(col)] for _ in range(row)]
    cnt = 0
    for r in range(row):
        for c in range(col):
            if graph[r][c] > 0 and not visited[r][c]:
                if cnt:
                    return 2
                DFS(r, c, visited)
                cnt += 1
    return cnt


def pass_year():
    for r in range(1, row-1):
        for c in range(1, col-1):
            cnt = 0
            for k in move:
                new_row = r + k[0]
                new_col = c + k[1]
                if not freeze[new_row][new_col]:
                    cnt += 1
            graph[r][c] -= cnt
            if graph[r][c] < 0:
                graph[r][c] = 0

    for r in range(row):
        for c in range(col):
            if graph[r][c] <= 0:
                freeze[r][c] = 0


ans = 0
while True:
    temp = check_split()
    if temp >= 2:
        break
    elif temp == 0:
        ans = 0
        break
    else:
        pass_year()
        ans += 1
print(ans)

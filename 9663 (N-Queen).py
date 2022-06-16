n = int(input().strip())
graph = [-1 for _ in range(n)]
visited = [False for _ in range(n)]
cnt = 0


def check(idx, i):
    for j in range(idx):
        if graph[j] == i or abs(i - graph[j]) == abs(idx - j):
            return False
    return True


def recursive(idx):
    if idx == n-1:
        global cnt
        cnt += 1
        return

    for i in range(n):
        if visited[i]:
            continue

        if check(idx+1, i):
            graph[idx+1] = i
            visited[i] = True
            recursive(idx+1)
            visited[i] = False


for k in range(n):
    graph[0] = k
    recursive(0)

print(cnt)
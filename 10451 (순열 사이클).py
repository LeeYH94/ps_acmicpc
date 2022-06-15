import sys
T = int(input())

for _ in range(T):
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    lst.insert(0, 0)
    visited = [0 for _ in range(n+1)]
    cnt = 0

    for i in range(1, n+1):
        if not visited[i]:
            cnt += 1
            visited[i] = 1
            while not visited[lst[i]]:
                visited[lst[i]] = 1
                i = lst[i]
    print(cnt)

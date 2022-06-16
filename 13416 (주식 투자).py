import sys
n = int(sys.stdin.readline().strip())
for _ in range(n):
    ans = 0
    num = int(sys.stdin.readline().strip())
    for i in range(num):
        a, b, c = map(int, sys.stdin.readline().split())
        ans += max(0, a, b, c)
    print(ans)
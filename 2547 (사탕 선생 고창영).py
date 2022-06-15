import sys
for _ in range(int(input())):
    s = input()
    n = int(sys.stdin.readline().rstrip())
    ans = 0
    for i in range(n):
        ans += int(sys.stdin.readline().rstrip())
    if ans % n == 0:
        print("YES")
    else:
        print("NO")
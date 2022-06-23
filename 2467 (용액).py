import sys
n = int(sys.stdin.readline().strip())
lst = list(map(int, sys.stdin.readline().split()))

e = n-1
a, b = 0, 0
ans = 10 ** 15

for s in range(n):
    while e >= 0 and e != s:
        temp = lst[s] + lst[e]
        if abs(temp) < ans:
            ans = abs(temp)
            a, b = lst[s], lst[e]
        if temp > 0:
            e -= 1
        else:
            break
print(a, b)
import sys
n, b = sys.stdin.readline().split()
b = int(b)
n = n[::-1]
ans = 0
for i in range(len(n)):
    if n[i].isdigit():
        ans += int(n[i]) * (b ** i)
    else:
        ans += (ord(n[i]) - 55) * (b ** i)
print(ans)
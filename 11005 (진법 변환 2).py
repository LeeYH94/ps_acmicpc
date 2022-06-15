import sys
n, b = map(int, sys.stdin.readline().split())
s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = ""

while n != 0:
    ans += str(s[n%b])
    n //= b
print(ans[::-1])
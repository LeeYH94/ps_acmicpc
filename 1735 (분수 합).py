from math import gcd

a, b = map(int, input().split())
c, d = map(int, input().split())
x = a * d + c * b
y = b * d
z = gcd(x, y)
print(str(x//z) + ' ' + str(y//z))
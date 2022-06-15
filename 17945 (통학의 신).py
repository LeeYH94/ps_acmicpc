from math import sqrt
b, c = map(int, input().split())
x1 = int(-b + sqrt(b**2 - c))
x2 = int(-b - sqrt(b**2 - c))
if x1 < x2:
    print("{} {}".format(x1, x2))
elif x1 > x2:
    print("{} {}".format(x2, x1))
else:
    print(x1)
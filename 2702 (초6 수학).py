import math
for i in range(int(input())):
    a, b = map(int, input().split())
    print((a * b)//math.gcd(a, b), end = ' ')
    print(math.gcd(a, b))

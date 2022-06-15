from math import gcd
a, b = map(int, input().split(':'))
print(str(a // gcd(a, b)) + ':' + str(b // gcd(a, b)))

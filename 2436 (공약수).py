from math import gcd
A, B = map(int, input().split())
n = A * B
lst = []
for i in range(1, b**1//2):
    if i * (n // i) == gcd(i, n//i) and gcd(i, n // i) // n == 1:
        lst.append([i, n//i])
print(lst)

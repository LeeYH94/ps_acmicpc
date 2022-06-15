from math import sqrt
def isPrime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
a, b = map(int, input().split())
lst = []
for i in range(2, b + 1):
    if isPrime(i) == True:
        lst.append(i)
if b == 1:
    print()
elif b == 2:
    print(2)
else:
    for i in lst:
        if i >= a:
            print(i)

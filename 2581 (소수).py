from math import sqrt

def isPrime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


a = int(input())
b = int(input())
total = 0
lst = []
for i in range(a, b + 1):
    if isPrime(i) == True and i != 1:
        total += i
        lst.append(i)
if b == 1:
    print(-1)
elif b == 2:
    print(2)
    print(2)
elif len(lst) == 0:
    print(-1)
else:
    print(total)
    print(lst[0])

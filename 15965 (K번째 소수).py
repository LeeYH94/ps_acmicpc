from math import sqrt
def isPrime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


n = int(input())
if n == 1:
    print(2)
    exit()
elif n == 2:
    print(3)
    exit()
lst = []
i = 2
while len(lst) < n:
    if isPrime(i):
        lst.append(i)
    i += 1
print(lst[-1])


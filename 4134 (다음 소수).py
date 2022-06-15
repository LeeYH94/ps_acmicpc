from math import sqrt
def isPrime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
for _ in range(int(input())):
    num = int(input())
    if num == 0 or num == 1 or num == 2:
        print(2)
        continue

    for i in range(num, 4 * (10 ** 10)+1):
        if isPrime(i):
            print(i)
            break
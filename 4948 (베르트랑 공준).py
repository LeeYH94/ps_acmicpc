from math import sqrt
def isPrime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


lst = [2]
for i in range(3, 123456 * 2 + 1):
    if isPrime(i):
        lst.append(i)
s = set(lst)
while True:
    n = int(input())
    cnt = 0
    if n == 0:
        break
    for i in lst:
        if n < i <= 2 * n and i in s:
            cnt += 1
    print(cnt)
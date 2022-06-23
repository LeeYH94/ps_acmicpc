import math
n = int(input().strip())
lst = []


def isPrime(a):
    if a < 2:
        return False
    for i in range(2, int(math.sqrt(a))+1):
        if a % i == 0:
            return False
    return True


for i in range(n+1):
    if isPrime(i):
        lst.append(i)


e = 0
interval = 0
cnt = 0

for s in range(len(lst)):
    while interval < n and e < len(lst):
        interval += lst[e]
        e += 1
    if interval == n:
        cnt += 1
    interval -= lst[s]
    s += 1

print(cnt)
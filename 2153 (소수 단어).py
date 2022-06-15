from math import sqrt
def isPrime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
s = input()
ans = 0
for i in s:
    if 65 <= ord(i) <= 90:
        ans += ord(i) - 38
    else:
        ans += ord(i) - 96
if ans == 1:
    print("It is a prime word.")
    exit()
if ans == 2:
    print("It is a prime word.")
    exit()
if isPrime(ans):
    print("It is a prime word.")
else:
    print("It is not a prime word.")
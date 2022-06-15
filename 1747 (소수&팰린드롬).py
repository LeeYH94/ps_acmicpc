from math import sqrt


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


k = int(input())
if k == 1:
    print(2)
    exit()
while 1:
    if is_prime(k):
        if str(k)[::-1] == str(k):
            print(k)
            exit()
    k += 1

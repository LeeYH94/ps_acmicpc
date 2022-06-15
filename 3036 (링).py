from math import gcd

n = int(input())
lst = list(map(int, input().split()))
for i in range(1, len(lst)):
    g = gcd(lst[0], lst[i])
    print("{}/{}".format(lst[0] // g, lst[i] // g))

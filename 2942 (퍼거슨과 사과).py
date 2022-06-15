import math
a, b = map(int, input().split())
c = math.gcd(a, b)
lst = []
for i in range(1, int(math.sqrt(c)) + 1):
    if c % i == 0:
        lst.append(i)
        lst.append(c//i)
s1 = set(lst)
lst2 = sorted(list(s1))

for i in lst2:
    print("{} {} {}".format(i, a//i, b//i))
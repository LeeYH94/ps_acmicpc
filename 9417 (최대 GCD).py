from math import gcd
for _ in range(int(input())):
    lst = list(map(int, input().split()))
    lst2 = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j:
                lst2.append(gcd(lst[i], lst[j]))
    lst2.sort()
    print(lst2[-1])
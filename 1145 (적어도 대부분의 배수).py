from math import gcd
lst = list(map(int, input().split()))
temp_lst = []
for i in range(len(lst)):
    for j in range(len(lst)):
        for k in range(len(lst)):
            if i != j and j != k and i != k:
                temp = (lst[i] * lst[j]) // gcd(lst[i], lst[j])
                temp_lst.append((temp * lst[k]) // gcd(temp, lst[k]))
temp_lst.sort()
print(temp_lst[0])
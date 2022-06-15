n = input()
lst = list(map(int, input().split()))

lst2 = [25]
for i in range(11, 80001):
    if i % 3 == 0 or i % 7 == 0:
        lst2.append(lst2[-1] + i)
    else:
        lst2.append(lst2[-1])
for i in lst:
    print(lst2[i-10])
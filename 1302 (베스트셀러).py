n = int(input())
lst1 = [0] * n
lst2 = []
for i in range(n):
    s = input()
    if s not in lst2:
        lst2.append(s)
        lst1[lst2.index(s)] += 1
    if s in lst2:
        lst1[lst2.index(s)] += 1
max_val = lst1[0]
for i in range(1, len(lst2)):
    if lst1[i] > max_val:
        max_val = lst1[i]
if lst1.count(max_val) == 1:
    print(lst2[lst1.index(max_val)])
else:
    lst3 = []
    for i in range(len(lst2)):
        if lst1[i] == max_val:
            lst3.append(lst2[i])
    lst3.sort()
    print(lst3[0])

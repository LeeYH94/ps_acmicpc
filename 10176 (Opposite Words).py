s1 = 'abcdefghijklmnopqrstuvwxyz'
s2 = s1[::-1]
for _ in range(int(input())):
    lst1 = []
    lst2 = []
    s = input().lower()
    for i in s:
        if i in s1:
            lst1.append(i)
            lst2.append(s2[s1.index(i)])
    lst1.sort()
    lst2.sort()
    if lst1 == lst2:
        print("Yes")
    else:
        print('No')
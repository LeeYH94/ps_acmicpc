n = int(input())
lst = []
for i in range(n):
    lst.append(input()[::-1])
for i in range(len(lst[0])):
    lst1 = []
    for j in range(n):
        lst1.append(lst[j][0:i+1])
    s1 = set(lst1)
    if len(s1) == len(lst1):
        print(i+1)
        exit()
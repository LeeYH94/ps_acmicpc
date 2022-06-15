a, b = input().split()
s1 = set(list(map(int, input().split())))
s2 = set(list(map(int, input().split())))
lst = list(s1 - s2)
print(len(lst))
if len(lst) != 0:
    lst.sort()
    for i in lst:
        print(i, end = ' ')

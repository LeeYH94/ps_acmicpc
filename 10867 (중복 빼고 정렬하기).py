n = int(input())
s1 = set(list(map(int, input().split())))
lst = list(s1)
lst.sort()

for i in range(len(lst)):
    print(lst[i], end = ' ')

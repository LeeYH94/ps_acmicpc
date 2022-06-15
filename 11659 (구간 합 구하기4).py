import sys
a, b = map(int, input().split())
lst1 = list(map(int, input().split()))
lst2 = []
temp = 0
for i in lst1:
    temp += i
    lst2.append(temp)
for _ in range(b):
    i, j = map(int, sys.stdin.readline().split())
    if i == 1:
        print(lst2[j-1])
    else:
        print(lst2[j-1] - lst2[i-2])
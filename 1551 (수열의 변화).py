a, b = map(int, input().split())
lst = list(map(int, input().split(',')))
for i in range(b):
    lst2 = [0] * (len(lst)-1)
    for j in range(len(lst)-1):
        lst2[j] = lst[j+1] - lst[j]
    lst = lst2
for i in range(len(lst)-1):
    print(lst[i], end=',')
print(lst[-1])
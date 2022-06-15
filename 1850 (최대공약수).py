a, b = input().split()
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
lst = l1 + l2
lst.sort()
for i in range(len(lst)):
    print(lst[i], end = ' ')

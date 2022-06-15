a, b = map(int, input().split())
lst1 = []
lst2 = []
lst3 = []
for _ in range(a):
    lst1.append(list(map(int, input().split())))
for _ in range(a):
    lst2.append(list(map(int, input().split())))
for i in range(a):
    for j in range(b):
        lst3.append(lst1[i][j] + lst2[i][j])
for i in range(a*b):
    if (i+1) % b == 0:
        print(lst3[i])
    else:
        print(lst3[i], end = ' ')
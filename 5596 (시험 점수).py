lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
r1 = 0
r2 = 0
for i in range(4):
    r1 += lst1[i]
    r2 += lst2[i]
print(r1 if r1 > r2 else r2)

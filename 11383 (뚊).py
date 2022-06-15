a, b = map(int, input().split())
lst1 = []
lst2 = []
ans = 'Eyfa'
for _ in range(a):
    lst1.append(input())
for _ in range(a):
    lst2.append(input())
for i in range(a):
    temp = ''
    for j in lst1[i]:
        temp += j * 2
    if temp != lst2[i]:
        ans = 'Not Eyfa'
print(ans)
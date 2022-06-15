lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

a = 0
b = 0
for i in range(len(lst1)):
    if lst1[i] > lst2[i]:
        a += 1
    elif lst1[i] < lst2[i]:
        b += 1
if a > b:
    print("A")
elif b > a:
    print("B")
else:
    print("D")
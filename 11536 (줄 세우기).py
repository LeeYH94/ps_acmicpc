lst1 = []
for _ in range(int(input())):
    lst1.append(input())
lst2 = sorted(lst1)
lst3 = sorted(lst1, reverse = True)

if lst1 == lst2:
    print("INCREASING")
elif lst1 == lst3:
    print("DECREASING")
else:
    print("NEITHER")
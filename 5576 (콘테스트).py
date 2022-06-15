lst1 = []
lst2 = []
for i in range(10):
    lst1.append(int(input()))
for i in range(10):
    lst2.append(int(input()))
lst1.sort(reverse=True)
lst2.sort(reverse=True)
n1 = lst1[0] + lst1[1] + lst1[2]
n2 = lst2[0] + lst2[1] + lst2[2]
print(str(n1) + " " + str(n2))
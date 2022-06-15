lst1 = []
lst2 = []
for _ in range(3):
    lst1.append(int(input()))
for _ in range(2):
    lst2.append(int(input()))
lst1.sort()
lst2.sort()
print(lst1[0] + lst2[0] - 50)

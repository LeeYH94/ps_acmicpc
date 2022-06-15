n = input()
lst = list(map(int, input().split()))
lst1 = []
lst2 = []
for i in range(len(lst)):
    if lst[i] == -1:
        lst2 = lst[i+1:]
        break
    lst1.append(lst[i])
lst1.sort()
lst2.sort()
print(lst1[0] + lst2[0])
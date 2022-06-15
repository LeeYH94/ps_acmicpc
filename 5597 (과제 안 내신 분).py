lst = []
lst2 = []
for i in range(1,31):
    lst2.append(i)
for i in range(28):
    lst.append(int(input()))
result = list(set(lst2) - set(lst))
result.sort()
for i in range(len(result)):
    print(result[i])

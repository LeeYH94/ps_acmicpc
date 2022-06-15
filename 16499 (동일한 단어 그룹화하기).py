lst = []
for _ in range(int(input())):
    s = input()
    temp = []
    for i in s:
        temp.append(i)
    temp.sort()
    if temp in lst:
        continue
    else:
        lst.append(temp)
print(len(lst))
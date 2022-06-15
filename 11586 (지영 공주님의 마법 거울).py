n = int(input())
lst = []
for i in range(n):
    lst.append(input())
num = int(input())
if num == 1:
    for i in lst:
        print(i)
elif num == 2:
    for i in lst:
        print(i[::-1])
else:
    for i in range(len(lst)-1, -1, -1):
        print(lst[i])

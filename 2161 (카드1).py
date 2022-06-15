n = int(input())
lst = []
for i in range(1, n+1):
    lst.append(i)
while len(lst) != 1:
    print(lst.pop(0), end=' ')
    lst.append(lst.pop(0))
print(lst[0])
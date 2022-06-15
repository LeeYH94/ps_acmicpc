lst1 = []
lst2 = []
s = ''
for _ in range(3):
    a, b = map(int, input().split())
    lst1.append(a)
    lst2.append(b)
for i in lst1:
    if lst1.count(i) == 1:
        s += str(i)
s += ' '
for i in lst2:
    if lst2.count(i) == 1:
        s += str(i)
print(s)

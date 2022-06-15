n = int(input())
temp = set()

for i in range(n):
    a, b = input().split()
    if b == 'enter':
        temp.add(a)
    elif b == 'leave':
        temp.remove(a)

lst = list(temp)
lst.sort(reverse = True)
if len(lst) != 0:
    for i in range(len(lst)):
        print(lst[i])
else:
    print()

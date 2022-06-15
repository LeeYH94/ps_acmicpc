lst = list(map(int, input().split()))
s = input()
lst.sort()
a = lst[0]
b = lst[1]
c = lst[2]
for i in range(3):
    if s[i] == 'A':
        print(a, end = ' ')
    if s[i] == 'B':
        print(b, end = ' ')
    if s[i] == 'C':
        print(c, end = ' ')
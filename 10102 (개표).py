n = input()
s = input()
a = 0
b = 0
for i in s:
    if i == 'A':
        a += 1
    elif i == 'B':
        b += 1
if a > b:
    print('A')
elif b > a:
    print('B')
else:
    print('Tie')

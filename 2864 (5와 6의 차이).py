a, b = input().split()
s_a = ''
s_b = ''
l_a = ''
l_b = ''
for i in a:
    if i == '5' or i == '6':
        s_a += '5'
        l_a += '6'
    else:
        s_a += i
        l_a += i
for i in b:
    if i == '5' or i == '6':
        s_b += '5'
        l_b += '6'
    else:
        s_b += i
        l_b += i
print(int(s_a) + int(s_b), end=' ')
print(int(l_a) + int(l_b))
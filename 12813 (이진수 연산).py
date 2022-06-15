a = input()
b = input()
s1, s2, s3, s4, s5 = '', '', '', '', ''
for i in range(100000):
    if a[i] == '1' and b[i] == '1':
        s1 += '1'
    else:
        s1 += '0'

    if a[i] == '1' or b[i] == '1':
        s2 += '1'
    else:
        s2 += '0'

    if a[i] != b[i]:
        s3 += '1'
    else:
        s3 += '0'

    if a[i] == '0':
        s4 += '1'
    else:
        s4 += '0'

    if b[i] == '0':
        s5 += '1'
    else:
        s5 += '0'
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
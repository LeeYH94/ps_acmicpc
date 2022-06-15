a, b = map(int, input().split())
result = a
a = bin(a)[2:]
a = a[::-1] + '0' * 33
b = bin(b)[::-1]
c = ''
for i in range(len(a)):
    if a[i] == '1':
        c += '1'
    else:
        if b[0] == 'b':
            c += a[i:]
            break
        c += b[0]
        b = b[1:]
c = c[::-1]
c = int(c, 2)
result -= c
print(-result)
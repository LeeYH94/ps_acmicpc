lst = ['{}', '{{}}']
for i in range(2, 16):
    s = '{'
    for j in range(i):
        if j != i-1:
            s += lst[j] + ','
        else:
            s += lst[j]
    s += '}'
    lst.append(s)
for i in range(int(input())):
    a = input()
    b = input()
    idx_a = lst.index(a)
    idx_b = lst.index(b)
    print(lst[idx_a + idx_b])
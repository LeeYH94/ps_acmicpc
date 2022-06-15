s1 = '*.*.*.*.*.'
s2 = '.*.*.*.*.*'
a, b = map(int, input().split())
for i in range(a):
    if i % 2 == 0:
        print(s1[:b])
    else:
        print(s2[:b])

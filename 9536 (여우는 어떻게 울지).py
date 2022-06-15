import sys
for _ in range(int(input())):
    lst1 = list(input().split())
    s1 = set([])
    s = ''
    while 1:
        lst2 = sys.stdin.readline().split()
        if lst2[0] == 'what':
            break
        s1.add(lst2[2])
    for i in lst1:
        if i not in s1:
            s += i
            s += ' '
    print(s)

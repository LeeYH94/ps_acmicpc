while 1:
    s = input()
    if s == '#':
        break
    lst = s.split()
    lst2 = []
    for i in lst:
        lst2.append(i[::-1])
    for i in lst2:
        print(i, end = ' ')
    print()
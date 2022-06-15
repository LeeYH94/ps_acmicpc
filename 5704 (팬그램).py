while 1:
    s1 = set()
    s = input()
    if s == '*':
        break
    for i in s:
        if i != ' ':
            s1.add(i)
    if len(s1) == 26:
        print('Y')
    else:
        print('N')
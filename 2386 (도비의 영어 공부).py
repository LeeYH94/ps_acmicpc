while 1:
    s = input().lower()
    if s == '#':
        break
    alp = s[0]
    s = s[2:]
    result = 0
    for i in s:
        if alp == i:
            result += 1
    print('{} {}'.format(alp, result))
    

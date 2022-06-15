while 1:
    s = input()
    if s == '#':
        break
    s1 = ''
    one = 0
    for i in range(len(s)):
        if s[i] == '1':
            one += 1
        if s[i] == 'o' or s[i] == 'e':
            break
    if s[-1] == 'e':
        if one % 2 == 0:
            s1 = s[:-1] + '0'
        else:
            s1 = s[:-1] + '1'
    elif s[-1] == 'o':
        if one % 2 == 0:
            s1 = s[:-1] + '1'
        else:
            s1 = s[:-1] + '0'
    print(s1)
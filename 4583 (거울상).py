while 1:
    s = input()
    if s == '#':
        break
    s = s[::-1]
    s2 = ''
    for i in range(len(s)):
        if s[i] == 'b':
            s2 += 'd'
        elif s[i] == 'd':
            s2 += 'b'
        elif s[i] == 'q':
            s2 += 'p'
        elif s[i] == 'p':
            s2 += 'q'
        elif s[i] == 'i' or s[i] == 'o' or s[i] == 'v' or s[i] == 'w' or s[i] == 'x':
            s2 += s[i]
        else:
            s2 = 'INVALID'
            break
    print(s2)
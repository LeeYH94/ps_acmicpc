while 1:
    s = input()
    result = 0
    if s == '#':
        break
    for i in range(len(s)):
        if s[i] == ' ':
            continue
        else:
            result += (ord(s[i]) - 64) * (i + 1)
    print(result)
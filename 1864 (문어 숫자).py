while 1:
    s = input()
    if s == "#":
        break
    ans = []
    for i in s:
        if i == '-':
            ans.append('0')
        elif i == '\\':
            ans.append('1')
        elif i == '(':
            ans.append('2')
        elif i == '@':
            ans.append('3')
        elif i == '?':
            ans.append('4')
        elif i == '>':
            ans.append('5')
        elif i == '&':
            ans.append('6')
        elif i == '%':
            ans.append('7')
        elif i == '/':
            ans.append('-1')
    ans.reverse()
    result = 0
    for i in range(len(ans)):
        result += 8 ** i * int(ans[i])
    print(result)
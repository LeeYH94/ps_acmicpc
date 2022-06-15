for _ in range(int(input())):
    s = input()
    s1 = input()
    s2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ans = ''
    for i in s:
        for j in range(len(s2)):
            if i == s2[j]:
                ans += s1[j]
        if i == ' ':
            ans += ' '
    print(ans)
for _ in range(int(input())):
    s = input()
    ans = 0
    for i in range(len(s)):
        if i % 2 == 0:
            if int(s[i]) * 2 >= 10:
                ans += int(s[i]) * 2 % 10 + 1
            else:
                ans += int(s[i]) * 2
        else:
            ans += int(s[i])
    if ans % 10 == 0:
        print('T')
    else:
        print('F')
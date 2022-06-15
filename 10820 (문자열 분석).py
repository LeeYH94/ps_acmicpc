while 1:
    try:
        small = 0
        big = 0
        num = 0
        blank = 0
        s = input()
        for i in range(len(s)):
            if 65 <= ord(s[i]) <= 90:
                big += 1
            elif 97 <= ord(s[i]) <= 122:
                small += 1
            elif s[i] == ' ':
                blank += 1
            else:
                num += 1
        print("{} {} {} {}".format(small, big, num, blank))
    except EOFError:
        break

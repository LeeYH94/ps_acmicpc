for _ in range(3):
    s = input()
    cnt = 1
    max_num = 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            cnt += 1
            if cnt >= max_num:
                max_num = cnt
        else:
            if cnt >= max_num:
                max_num = cnt
            cnt = 1
    print(max_num)

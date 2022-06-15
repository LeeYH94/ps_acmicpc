while 1:
    try:
        n = int(input())
        ans = 1
        cnt = 1
        while ans % n != 0:
            ans = ans * 10 + 1
            cnt += 1
        print(cnt)
    except EOFError:
        break
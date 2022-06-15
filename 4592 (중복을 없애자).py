while 1:
    lst = list(map(int, input().split()))
    if lst[0] == 0:
        break
    print(lst[1], end = ' ')
    for i in range(2, len(lst)):
        if lst[i] == lst[i - 1]:
            continue
        else:
            print(lst[i], end = ' ')
    print('$')
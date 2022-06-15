for _ in range(int(input())):
    lst = list(input().split())
    num = float(lst[0])
    for i in range(1, len(lst)):
        if lst[i] == '@':
            num *= 3
        elif lst[i] == '%':
            num += 5
        elif lst[i] == '#':
            num -= 7
    print("%.2f" % num)

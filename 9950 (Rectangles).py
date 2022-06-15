while 1:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    if a == 0:
        a = c // b
    elif b == 0:
        b = c // a
    elif c == 0:
        c = a * b
    print("{} {} {}".format(a, b, c))
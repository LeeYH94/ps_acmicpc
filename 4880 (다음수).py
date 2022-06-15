while 1:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    if c - b == b - a:
        print("AP " + str(c + c - b))
    else:
        print("GP " + str(c * c // b))
while 1:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    if (c - a) % b != 0 or (c-a)//b +1 <= 0:
        print("X")
    else:
        print((c-a)//b + 1)

for _ in range(int(input())):
    p1 = 0
    p2 = 0
    for i in range(int(input())):
        a, b = input().split()
        if a == "R":
            if b == "P":
                p2 += 1
            elif b == "S":
                p1 += 1
        elif a == "P":
            if b == "R":
                p1 += 1
            elif b == "S":
                p2 += 1
        else:
            if b == "P":
                p1 += 1
            elif b == "R":
                p2 += 1
    if p1 == p2:
        print("TIE")
    elif p1 > p2:
        print("Player 1")
    else:
        print("Player 2")
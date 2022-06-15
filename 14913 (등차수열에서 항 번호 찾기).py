a, b, c = map(int, input().split())
if (c-a) % b != 0 or (c-a) // b < 0:
    print("X")
else:
    print((c-a) // b + 1)
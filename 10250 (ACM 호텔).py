for i in range(int(input())):
    h, w, n = map(int, input().split())
    a = n % h
    b = n // h + 1
    if a == 0:
        a = h
        b -= 1
    print(100 * a + b)

while 1:
    n = int(input())
    if n == 0:
        break
    if 1000000 < n <= 5000000:
        print(n // 10 * 9)
    elif n > 5000000:
        print(n // 10 * 8)
    else:
        print(n)
for _ in range(int(input())):
    a, b = input().split()
    if b == 'C':
        lst = input().split()
        for i in lst:
            print(ord(i) - 64, end = ' ')
        print()

    else:
        lst = list(map(int, input().split()))
        for i in lst:
            print(chr(i + 64), end = ' ')
        print()

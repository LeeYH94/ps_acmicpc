for _ in range(int(input())):
    lst = input().split()
    s = ""
    for i in lst:
        s += i[::-1]
        s += ' '
    print(s)
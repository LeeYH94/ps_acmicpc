for _ in range(int(input())):
    n = input()
    if len(n) == 1:
        print(n)
    else:
        lst = list(map(int, n[::-1]))
        if lst[-1] >= 5:
            lst.append(0)
        for i in range(len(lst)-1):
            if lst[i] >= 5:
                lst[i+1] += 1
            lst[i] = 0
        s = ''
        for i in lst:
            s += str(i)
        print(s[::-1])


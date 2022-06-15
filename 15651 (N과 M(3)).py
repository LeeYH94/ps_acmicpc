n, m = map(int, input().split())
lst = [1] * m
if m == 1:
    for i in range(1, n + 1):
        print(i)
else:
    while lst != [n] * m:
        for i in range(0, m):
            print(lst[i], end=' ')
        print()
        lst[m - 1] += 1
        for i in range(m - 1, 0, -1):
            if lst[i] > n:
                lst[i - 1] += 1
                lst[i] = 1
    for i in lst:
        print(i, end = ' ')
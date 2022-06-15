n = int(input())

for i in range(n):
    x = int(input())
    lst = [0] * 101
    lst[0] = 0
    lst[1] = 1
    lst[2] = 1
    lst[3] = 1
    if x > 3:
        for i in range(4, x+1):
            lst[i] = lst[i - 2] + lst[i - 3]
    print(lst[x])

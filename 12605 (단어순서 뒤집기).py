for i in range(int(input())):
    lst = list(input().split())
    lst = reversed(lst)
    print("Case #{}: ".format(i + 1), end = '')
    for i in lst:
        print(i, end = ' ')
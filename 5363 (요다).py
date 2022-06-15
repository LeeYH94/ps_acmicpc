for _ in range(int(input())):
    lst = list(input().split())
    for i in range(2,len(lst)):
        print(lst[i], end = ' ')
    print(lst[0], end = ' ')
    print(lst[1])

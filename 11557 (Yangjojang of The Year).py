for _ in range(int(input())):
    lst = []
    s = ''
    max_num = 0
    for i in range(int(input())):
        lst.append(input().split())
        if int(lst[i][1]) > max_num:
            max_num = int(lst[i][1])
            s = lst[i][0]
    print(s)

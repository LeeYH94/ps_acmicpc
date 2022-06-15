for _ in range(int(input())):
    lst = list(map(int, input().split()))
    total = 0
    min_num = 10000000
    for i in lst:
        if i % 2 == 0:
            total += i
            if i < min_num:
                min_num = i
    print("{} {}".format(total, min_num))
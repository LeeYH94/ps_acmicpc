for _ in range(int(input())):
    lst = list(map(int, input().split()))
    lst = sorted(lst)
    if lst[3] - lst[1] > 3:
        print("KIN")
    else:
        print(lst[1] + lst[2] + lst[3])
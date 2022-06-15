cnt = 1
for _ in range(int(input())):
    lst = list(input().split())
    lst[0] = int(lst[0])
    lst[2] = int(lst[2])
    lst[4] = int(lst[4])
    if lst[1] == '+':
        if lst[0] + lst[2] == lst[4]:
            print("Case {}: YES".format(cnt))
        else:
            print("Case {}: NO".format(cnt))
    else:
        if lst[0] - lst[2] == lst[4]:
            print("Case {}: YES".format(cnt))
        else:
            print("Case {}: NO".format(cnt))
    cnt += 1
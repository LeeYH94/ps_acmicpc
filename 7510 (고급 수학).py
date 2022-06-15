n = int(input())
for i in range(n):
    lst = list(map(int, input().split()))
    lst = sorted(lst)
    if lst[0] ** 2 + lst[1] ** 2 == lst[2] ** 2:
        print("Scenario #{}:".format(i + 1))
        print('yes')
        if i == n-1:
            continue
        print()
    else:
        print("Scenario #{}:".format(i + 1))
        print('no')
        if i == n - 1:
            continue
        print()
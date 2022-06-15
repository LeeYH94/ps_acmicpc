lst = list(map(int, input().split()))
temp = sorted(lst)
while temp != lst:
    for i in range(4):
        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
            for j in lst:
                print(j, end = ' ')
            print()

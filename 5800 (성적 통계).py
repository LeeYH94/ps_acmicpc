for i in range(int(input())):
    print("Class " + str(i + 1))
    lst = list(map(int, input().split()))
    lst.pop(0)
    lst.sort(reverse = True)
    max_val = lst[0]
    min_val = lst[-1]
    max_gap = 0
    for j in range(len(lst) - 1):
        if lst[j] - lst[j + 1] > max_gap:
            max_gap = lst[j] - lst[j + 1]
    print("Max " + str(max_val) + ", Min " + str(min_val) + ", Largest gap " + str(max_gap))

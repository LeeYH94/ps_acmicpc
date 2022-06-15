max_num = 0
row = 0
col = 0
for i in range(9):
    lst = list(map(int, input().split()))
    for j in range(len(lst)):
        if lst[j] > max_num:
            row = i + 1
            col = j + 1
            max_num = lst[j]
print(max_num)
print("{} {}".format(row, col))
n = int(input())
lst = [[0, 1], [1, 1]]
for i in range(2, 46):
    lst.append([lst[i-2][0] + lst[i-1][0], lst[i-2][1] + lst[i-1][1]])
print(str(lst[n-1][0]) + " " + str(lst[n-1][1]))
lst = []
for i in range(int(input())):
    t_lst = list(map(int, input().split()))
    lst.append(t_lst)
result = []
for i in range(len(lst)):
    count = 0
    for j in range(len(lst)):
        if i != j:
            if lst[j][0] > lst[i][0] and lst[j][1] > lst[i][1]:
                count += 1
    result.append(count + 1)
for i in result:
    print(i, end = ' ')

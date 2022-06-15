while 1:
    lst = list(map(int, input().split()))
    if lst[0] == 0 and lst[1] == 0 and lst[2] == 0 and lst[3] == 0:
        break
    else:
        cnt = 0
        while len(set(lst)) != 1:
            lst = [abs(lst[0]-lst[1]), abs(lst[1]-lst[2]), abs(lst[2]-lst[3]), abs(lst[3]-lst[0])]
            cnt += 1
        print(cnt)
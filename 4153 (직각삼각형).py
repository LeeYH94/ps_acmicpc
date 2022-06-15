import sys
while 1:
    lst = list(map(int, sys.stdin.readline().split()))
    if lst[0] == 0 and lst[1] == 0 and lst[2] == 0:
        break
    lst.sort()
    if lst[0] * lst[0] + lst[1] * lst[1] == lst[2] * lst[2]:
        print('right')
    else:
        print('wrong')

import sys
case = 1
while 1:
    lst = list(sys.stdin.readline().split())
    ans = 'false'
    lst[0] = int(lst[0])
    lst[2] = int(lst[2])
    if lst[1] == 'E':
        break
    if lst[1] == '>':
        if lst[0] > lst[2]:
            ans = 'true'
    if lst[1] == '>=':
        if lst[0] >= lst[2]:
            ans = 'true'
    if lst[1] == '<':
        if lst[0] < lst[2]:
            ans = 'true'
    if lst[1] == '<=':
        if lst[0] <= lst[2]:
            ans = 'true'
    if lst[1] == '==':
        if lst[0] == lst[2]:
            ans = 'true'
    if lst[1] == '!=':
        if lst[0] != lst[2]:
            ans = 'true'
    print("Case " + str(case) + ": " + ans)
    case += 1
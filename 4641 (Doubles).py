while 1:
    lst = list(map(int, input().split()))
    s1 = set(lst)
    ans = 0
    if len(lst) == 1 and lst[0] == -1:
        break
    for i in range(len(lst)-1):
        if lst[i] * 2 in s1:
            ans += 1
    print(ans)
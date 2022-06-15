for _ in range(int(input())):
    s1 = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    s = set(input())
    lst = list(s1 - s)
    ans = 0
    for i in lst:
        ans += ord(i)
    print(ans)


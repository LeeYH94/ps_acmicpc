for _ in range(int(input())):
    s = input()
    num = int(len(s) ** 0.5)
    lst = []
    ans = ''
    for i in range(num):
        lst.append(s[i*num:i*num+num])
    for i in range(num-1, -1, -1):
        for j in range(num):
            ans += lst[j][i]
    print(ans)
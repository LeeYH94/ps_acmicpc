lst = []
while 1:
    n = float(input())
    if n == 999:
        for i in range(len(lst) - 1):
            print('%.2f' % (-lst[i] + lst[i+1]))
        break
    lst.append(n)
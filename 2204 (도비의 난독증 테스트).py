while 1:
    n = int(input())
    if n == 0:
        break
    lst = []
    for i in range(n):
        lst.append(input())
    lst = sorted(lst, key = lambda s : s.lower())
    print(lst[0])
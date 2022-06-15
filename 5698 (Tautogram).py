while 1:
    s = input().lower()
    if s == "*":
        break
    lst = list(s.split())
    s1 = set()
    for i in lst:
        s1.add(i[0])
    if len(s1) == 1:
        print('Y')
    else:
        print("N")
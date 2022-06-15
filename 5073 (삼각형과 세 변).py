while 1:
    a, b, c = list(map(int, input().split()))
    if a == 0 and b == 0 and c == 0:
        break
    lst = [a, b, c]
    lst.sort()
    if lst[0] + lst[1] <= lst[2]:
        print('Invalid')
        continue
    s1 = set(lst)
    if len(s1) == 3:
        print('Scalene')
    elif len(s1) == 2:
        print('Isosceles')
    else:
        print('Equilateral')
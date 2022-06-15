import sys
lst = []
for i in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().split()
    if s == ['pop']:
        if len(lst) != 0:
            print(lst[-1])
            lst.pop()
        else:
            print(-1)
    elif s == ['size']:
        print(len(lst))
    elif s == ['empty']:
        if len(lst) == 0:
            print(1)
        else:
            print(0)
    elif s == ['top']:
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])
    else:
        lst.append(s[1])
    

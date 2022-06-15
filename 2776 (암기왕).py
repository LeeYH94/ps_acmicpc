import sys
for _ in range(int(input())):
    a = sys.stdin.readline()
    s1 = set(map(int, sys.stdin.readline().split()))
    b = sys.stdin.readline()
    lst2 = list(map(int, sys.stdin.readline().split()))
    for i in lst2:
        if i in s1:
            print(1)
        else:
            print(0)

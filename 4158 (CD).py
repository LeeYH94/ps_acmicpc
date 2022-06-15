import sys
while 1:
    a, b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0:
        break
    s1 = set()
    s2 = set()
    for _ in range(a):
        s1.add(int(sys.stdin.readline().rstrip()))
    for _ in range(b):
        s2.add(int(sys.stdin.readline().rstrip()))
    print(len(s1 & s2))
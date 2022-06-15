import sys
for _ in range(int(input())):
    lst = []
    a, b, c = map(int, sys.stdin.readline().split())
    lst.append((a + b) ** 2 + c ** 2)
    lst.append((a + c) ** 2 + b ** 2)
    lst.append((b + c) ** 2 + a ** 2)
    lst.sort()
    print(lst[0])
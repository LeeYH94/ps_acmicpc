import sys
lst = []
for _ in range(int(input())):
    lst.append(list(map(int, sys.stdin.readline().split())))
lst = sorted(lst, key = lambda x: (x[0], x[1], x[2]))

for i in lst:
    print("{} {} {}".format(i[0], i[1], i[2]))

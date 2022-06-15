import sys
import operator
lst = []
for _ in range(int(input())):
    lst.append(list(map(int, sys.stdin.readline().split())))
lst = sorted(lst, key = operator.itemgetter(0, 1))

for i in lst:
    print("{} {}".format(i[0], i[1]))

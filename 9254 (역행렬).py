import numpy as np
import sys


def isint(num):
    num = round(num, 7)
    if num == int(num):
        return int(num)
    else:
        return num


n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, sys.stdin.readline().split(' '))))
a = np.array(lst)

try:
    b = np.linalg.inv(a)
    for i in range(n):
        for j in range(n):
            print(isint(b[i][j]), end=' ')
        print()
except np.linalg.LinAlgError:
    print("no inverse")
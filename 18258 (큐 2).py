import sys
from collections import deque

deq = deque()
x = ""
for _ in range(int(input())):
    x = sys.stdin.readline()
    if x[0:3] == "pop":
        if len(deq):
            print(deq.popleft())
        else:
            print(-1)
    elif x[0:4] == "size":
        print(len(deq))
    elif x[0:4] == "back":
        if len(deq):
            print(deq[-1])
        else:
            print(-1)
    elif x[0:4] == "push":
        num = int(x[5:])
        deq.append(num)
    elif x[0:5] == "empty":
        if len(deq):
            print(0)
        else:
            print(1)
    elif x[0:5] == "front":
        if len(deq):
            print(deq[0])
        else:
            print(-1)
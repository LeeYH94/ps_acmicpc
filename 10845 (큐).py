import collections
import sys
deq = collections.deque([])
for i in range(int(input())):
    s = sys.stdin.readline().rstrip()
    if s == 'pop':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())
    elif s == 'size':
        print(len(deq))
    elif s == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif s == 'front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    elif s == 'back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])
    else:
        deq.append(s[5:])

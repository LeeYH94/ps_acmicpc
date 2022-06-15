import collections

deq = collections.deque([])
for i in range(int(input()), 0, -1):
    deq.append(i)
while len(deq) != 1:
    deq.pop()
    deq.rotate(1)
print(deq[0])

import sys
n = int(sys.stdin.readline().rstrip())
lst = []
for _ in range(n):
    lst.append(int(sys.stdin.readline().rstrip()))
lst = lst[::-1]

h = 0
count = 0
for i in lst:
    if i > h:
        h = i
        count += 1
print(count)
import sys
lst = []
for _ in range(int(input())):
    a = sys.stdin.readline().rstrip()
    a = int(a)
    lst.append(a)

for i in lst:
    print(i)

import sys
aa = 0
bb = 0
for _ in range(int(input())):
    a, b = map(int, sys.stdin.readline().split())
    if a > b:
        aa += 1
    elif b > a:
        bb += 1
    else:
        continue
print(str(aa) + " " + str(bb))
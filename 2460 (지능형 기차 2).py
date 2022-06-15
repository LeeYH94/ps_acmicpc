import sys
maximum = 0
num = 0
for i in range(10):
    a, b = map(int, sys.stdin.readline().split())
    num -= a
    num += b
    if num >= maximum:
        maximum = num
print(maximum)
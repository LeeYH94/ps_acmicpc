import sys
n = int(sys.stdin.readline())
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    result = [(a ** j) % 10 for j in range(1, 5)][b % 4 - 1]
    print(result if result != 0 else 10)

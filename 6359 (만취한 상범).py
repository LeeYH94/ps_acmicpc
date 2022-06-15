import sys
for _ in range(int(sys.stdin.readline().rstrip())):
    escape = 0
    n = int(sys.stdin.readline().rstrip())
    for i in range(n+1):
        temp = 0
        for j in range(1, i+1):
            if i % j == 0:
                temp += 1
        if temp % 2 != 0:
            escape += 1
    print(escape)
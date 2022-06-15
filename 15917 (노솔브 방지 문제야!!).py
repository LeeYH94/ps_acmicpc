import sys
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    querry = True
    while(num != 1):
        if num % 2 != 0:
            querry = False
            break
        num /= 2
    if querry:
        print(1)
    else:
        print(0)
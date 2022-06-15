import sys
for _ in range(3):
    result = 0
    for i in range(int(input())):
        result += int(sys.stdin.readline().rstrip())

    if result == 0:
        print(0)
    elif result > 0:
        print('+')
    else:
        print('-')
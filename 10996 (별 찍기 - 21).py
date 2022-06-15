n = int(input())
for i in range(n*2):
    for j in range(n):
        if i % 2 == j % 2:
            print('*', end='')
        else:
            print(' ', end='')
    print()

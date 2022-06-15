n = int(input())

for i in range(n):
    print('*' * (i + 1), end = '')
    print(' ' * (2 * n - 2 * (i + 1)), end = '')
    print('*' * (i + 1))
for i in range(0, n - 1):
    print('*' * (n - i - 1), end = '')
    print(' ' * 2 * (i + 1), end = '')
    print('*' * (n - i - 1))

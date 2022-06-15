n = int(input())

for i in range(n, 1, -1):    
    print(' ' * (n - i), end = '')
    print('*' * (2 * i - 1))

print(' ' * (n - 1) + '*')

for i in range(1, n):
    print(' ' * (n - i - 1), end = '')
    print('*' * (2 * i + 1))

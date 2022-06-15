n = int(input())
a = '*'
b = ' '
for i in range(n-1 , -1 , -1):
    print(i*b + a)
    a += '*'

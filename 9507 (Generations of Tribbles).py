n = int(input())

for i in range(n):
    num = int(input())
    if num < 2:
        print(1)
    elif num == 2:
        print(2)
    elif num == 3:
        print(4)
    elif num > 3:
        a = 1
        b = 1
        c = 2
        d = 4
        for i in range(num - 3):
            a, b, c, d = b, c, d, a + b + c + d
        print(d)
        

for _ in range(int(input())):
    x = int(input())
    count = 1
    if x == 0:
        print(0)
    elif x == 1:
        print(2)
    else:
        a = 0
        b = 1
        while b != x:
            a, b = b, a + b
            count += 1
        print(count)
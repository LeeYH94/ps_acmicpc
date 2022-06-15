for i in range(int(input())):
    n = int(input())
    max_val = 0
    if n % 2 == 0 and n > 4:
        max_val = n
    elif n == 2 or n == 4:
        max_val = 4
    elif n == 1:
        max_val = 1
    else:
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = n * 3 + 1
                if n > max_val:
                    max_val = n
    print(max_val)

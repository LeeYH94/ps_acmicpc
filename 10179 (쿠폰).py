for _ in range(int(input())):
    n = float(input())
    n = n * 8 / 10
    num = round(n, 3)
    print('$%.2f' %num)
for _ in range(int(input())):
    n = int(input())
    temp = 0
    for i in range(n):
        if i + i ** 2 <= n:
            temp = i
        else:
            break
    print(temp)
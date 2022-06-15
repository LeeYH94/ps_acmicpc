for _ in range(int(input())):
    n = int(input())
    dict = {}
    for i in range(2, n+1):
        while n % i == 0:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
            n = n // i
        if n == 1:
            break
    lst = sorted(dict.items())
    for i in lst:
        print(i[0], end = " ")
        print(i[1])
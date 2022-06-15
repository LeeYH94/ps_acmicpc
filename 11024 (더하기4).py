for _ in range(int(input())):
    lst = list(map(int, input().split()))
    result = 0
    for i in lst:
        result += i
    print(result)
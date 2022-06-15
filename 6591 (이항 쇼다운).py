while 1:
    a, b = map(int, input().split())
    result = 1
    if a == 0 and b == 0:
        break
    if a - b < b:
        b = a - b
    for i in range(1, b + 1):
        result *= a
        result //= i
        a -= 1
    print(result)

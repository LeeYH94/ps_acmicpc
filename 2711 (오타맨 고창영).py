for _ in range(int(input())):
    result = ''
    a, b = input().split()
    a = int(a)
    result += b[:a-1]
    result += b[a:]
    print(result)
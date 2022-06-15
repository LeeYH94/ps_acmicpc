for _ in range(int(input())):
    a, b = input().split()
    a = int(a[::-1])
    b = int(b[::-1])
    print(str(int(str(a + b)[::-1])))
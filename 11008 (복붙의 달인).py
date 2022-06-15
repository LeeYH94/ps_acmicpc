for _ in range(int(input())):
    a, b = input().split()
    print(len(a) - a.count(b) * len(b) + a.count(b))
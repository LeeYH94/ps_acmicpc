for _ in range(int(input())):
    n = int(input())
    n = bin(n)[2:]
    n = n[::-1]
    for i in range(len(n)):
        if n[i] == '1':
            print(i, end = ' ')
    print()
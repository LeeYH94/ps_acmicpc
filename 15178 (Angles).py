for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a + b + c != 180:
        print('{} {} {} Check'.format(a, b, c))
    else:
        print('{} {} {} Seems OK'.format(a, b, c))
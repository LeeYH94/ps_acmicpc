a, b = input().split()
lst = [0] * (int(a) + 1)
for _ in range(int(b)):
    x, y, z = map(int, input().split())
    count = 0
    if x == 0:
        for i in range(y, z + 1):
            if lst[i] == 0:
                lst[i] = 1
            else:
                lst[i] = 0
    elif x == 1:
        for i in range(y, z + 1):
            if lst[i] == 1:
                count += 1
        print(count)

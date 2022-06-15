a, b = map(int, input().split())
temp = 1
for i in range(a):
    for j in range(b):
        if j == b-1:
            print(temp)
        else:
            print(temp, end=' ')
        temp += 1
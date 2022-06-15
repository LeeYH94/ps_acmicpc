n = input()
lst = list(map(int, input().split()))
for i in lst:
    if i == int(i ** 0.5) ** 2:
        print(1, end=" ")
    else:
        print(0, end=" ")
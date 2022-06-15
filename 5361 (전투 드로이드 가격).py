lst = [350.34, 230.90, 190.55, 125.30, 180.90]
for i in range(int(input())):
    lst1 = list(map(int, input().split()))
    num = 0
    for i in range(5):
        num += lst1[i] * lst[i]
    print("$%.2f" % num)
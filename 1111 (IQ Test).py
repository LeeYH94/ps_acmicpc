n = input()
lst = list(map(int, input().split()))
a = 0
b = 0
temp = 0
if len(lst) == 1:
    print('A')
elif len(lst) == 2:
    if lst[0] == lst[1]:
        print(lst[0])
    else:
        print('A')
else:
    if lst[1] - lst[0] == 0:
        a = 0
        b = lst[1]
    else:
        a = (lst[2] - lst[1]) // (lst[1] - lst[0])
        b = lst[1] - lst[0] * a
    for i in range(0, len(lst) - 1):
        if lst[i + 1] != lst[i] * a + b:
            print('B')
            exit()
    print(lst[-1] * a + b)

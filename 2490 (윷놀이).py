for i in range(3):
    yoot = 0
    lst = list(map(int, input().split()))
    for i in range(4):
        if lst[i] == 0:
            yoot += 1

    if yoot == 1:
        print('A')
    elif yoot == 2:
        print('B')
    elif yoot == 3:
        print('C')
    elif yoot == 4:
        print('D')
    else:
        print('E')

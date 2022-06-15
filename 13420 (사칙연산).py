for _ in range(int(input())):
    lst = input().split()
    if lst[1] == '*':
        if int(lst[0]) * int(lst[2]) == int(lst[4]):
            print('correct')
            continue
    elif lst[1] == '/':
        if int(lst[0]) / int(lst[2]) == int(lst[4]):
            print('correct')
            continue
    elif lst[1] == '+':
        if int(lst[0]) + int(lst[2]) == int(lst[4]):
            print('correct')
            continue
    elif lst[1] == '-':
        if int(lst[0]) - int(lst[2]) == int(lst[4]):
            print('correct')
            continue
    print('wrong answer')
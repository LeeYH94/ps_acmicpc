for i in range(int(input())):
    s = input()
    if s == 'P=NP':
        print('skipped')
    else:
        lst = s.split("+")
        print(int(lst[0]) + int(lst[1]))
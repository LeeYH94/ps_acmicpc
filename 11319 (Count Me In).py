s1 = set(['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'])
for _ in range(int(input())):
    s = input()
    lst = [0, 0]
    for i in s:
        if i in s1:
            lst[1] += 1
        elif i not in s1 and i != ' ':
            lst[0] += 1
    print("{} {}".format(lst[0], lst[1]))
import sys
lst = [[]]
for _ in range(int(sys.stdin.readline().rstrip())):
    s = sys.stdin.readline().rstrip()
    temp_lst = list([])
    if s[0] == 'a':
        temp_lst = lst[len(lst)-1]
        if not temp_lst:
            temp_lst = [s[2:]]
        else:
            temp_lst = temp_lst.append(s[2:])
        lst.append(temp_lst)
    if s[0] == 's':
        temp_lst = lst[len(lst)-1]
        if not temp_lst:
            lst.append([-1])
        else:
            temp_lst = temp_lst.pop()
            lst.append(temp_lst)
    if s[0] == 't':
        temp_lst = lst[int(s[2:])-1]
        lst.append(temp_lst)
print(lst)
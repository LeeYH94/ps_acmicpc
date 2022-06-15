n = int(input())
s1 = input()
s2 = input()
if n % 2 == 0:
    if s1 == s2:
        print('Deletion succeeded')
    else:
        print('Deletion failed')
else:
    check = True
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            check = False
    if check:
        print('Deletion succeeded')
    else:
        print('Deletion failed')
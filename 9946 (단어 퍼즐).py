case = 1
while 1:
    s1 = input()
    s2 = input()
    lst1 = []
    lst2 = []
    if s1 == "END" and s2 == "END":
        break
    for i in range(len(s1)):
        lst1.append(s1[i])
    for i in range(len(s2)):
        lst2.append(s2[i])
    lst1 = sorted(lst1)
    lst2 = sorted(lst2)
    if lst1 == lst2:
        print("Case {}: same".format(case))
    else:
        print("Case {}: different".format(case))
    case += 1
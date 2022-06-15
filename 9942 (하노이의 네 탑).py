lst = [1]
for i in range(2, 50):
    for j in range(i):
        lst.append(lst[-1] + 2 ** (i-1))

case = 1
while 1:
    try:
        print("Case {}: {}".format(case, lst[int(input())-1]))
        case += 1
    except EOFError:
        break
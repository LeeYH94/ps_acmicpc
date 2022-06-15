import sys
lst = []
for _ in range(int(input())):
    a, b, c, d = sys.stdin.readline().split()
    b = int(b)
    c = int(c)
    d = int(d)
    temp_lst = [a, b, c, d]
    lst.append(temp_lst)
lst = sorted(lst, key = lambda x: (x[3], x[2], x[1], x[0]))

print(lst[-1][0])
print(lst[0][0])

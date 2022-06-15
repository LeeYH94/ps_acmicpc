import itertools
lst = []
for i in range(9):
    lst.append(int(input()))
p = list(itertools.permutations(lst, 7))
for i in p:
    if sum(i) == 100:
        lst1 = list(i)
        for j in lst1:
            print(j)
        exit()
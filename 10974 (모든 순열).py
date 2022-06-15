import itertools

n = int(input())
lst = []
for i in range(1, n+1):
    lst.append(i)
per = list(itertools.permutations(lst))
for i in per:
    for j in range(len(i)):
        print(i[j], end = ' ')
    print()
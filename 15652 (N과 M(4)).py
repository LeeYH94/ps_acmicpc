import itertools

n, k = map(int, input().split())
lst = []
for i in range(1, n+1):
    lst.append(i)
per = list(itertools.combinations_with_replacement(lst, k))
for i in per:
    for j in range(len(i)):
        print(i[j], end = ' ')
    print()
import itertools

n, k = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
per = list(itertools.combinations_with_replacement(lst, k))
for i in per:
    for j in range(len(i)):
        print(i[j], end = ' ')
    print()
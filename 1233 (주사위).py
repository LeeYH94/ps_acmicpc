from collections import Counter
a, b, c = map(int, input().split())
lst = []
for i in range(1, a+1):
    for j in range(1, b+1):
        for k in range(1, c+1):
            lst.append(i + j + k)
lst = Counter(lst)
print(lst.most_common()[0][0])
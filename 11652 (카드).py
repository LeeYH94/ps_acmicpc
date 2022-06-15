from collections import Counter
n = int(input())
lst = []

for i in range(n):
    lst.append(int(input()))

dic = Counter(sorted(lst))
max_val = 0
for i in dic:
    if dic[i] > max_val:
        max_val = dic[i]
        index = i
print(index)

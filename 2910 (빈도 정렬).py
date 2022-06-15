from collections import Counter

a, b = input().split()
lst = list(map(int, input().split()))

lst2 = [items for items, c in Counter(lst).most_common() for item in [items] * c]
for i in lst2:
    print(i, end = ' ')
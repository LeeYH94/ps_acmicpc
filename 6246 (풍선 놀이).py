a, b = map(int, input().split())
lst = [0] * a
for _ in range(b):
    l, i = map(int, input().split())
    for j in range(l-1, a, i):
        lst[j] = 1
print(lst.count(0))
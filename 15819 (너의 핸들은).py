a, b = map(int, input().split())
lst = []
for _ in range(a):
    lst.append(input())
lst = sorted(lst)
print(lst[b - 1])
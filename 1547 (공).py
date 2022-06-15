lst = [1, 0, 0]
for _ in range(int(input())):
    a, b = map(int, input().split())
    lst[a-1], lst[b-1] = lst[b-1], lst[a-1]
print(lst.index(1) + 1)
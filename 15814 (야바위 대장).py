s = input()
lst = []
for i in s:
    lst.append(i)
for _ in range(int(input())):
    a, b = map(int, input().split())
    lst[a], lst[b] = lst[b], lst[a]
for i in lst:
    print(i, end='')
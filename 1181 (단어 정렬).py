n = int(input())
lst = [''] * n
for i in range(n):
    lst[i] = input()
lst = list(set(lst))
lst.sort()
lst.sort(key = len)

prev = ''
for i in range(len(lst)):
    print(lst[i])

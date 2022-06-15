a, b = input().split()
lst = [''] * int(a)
a = int(a)
for i in range(a):
    lst[i] = input()[::-1]
for i in range(a):
    print(lst[i])
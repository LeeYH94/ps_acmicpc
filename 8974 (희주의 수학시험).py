lst = []
cnt = 0
for i in range(1, 1001):
    for j in range(i):
        lst.append(i)
a, b = map(int , input().split())
for k in range(a-1, b):
    cnt += lst[k]
print(cnt)
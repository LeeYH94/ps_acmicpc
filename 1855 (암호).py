n = int(input())
s = input()
lst = []
ans = ''
for i in range(len(s)//n):
    lst.append(s[i*n:i*n + n])
for i in range(len(lst)):
    if i % 2 != 0:
        lst[i] = lst[i][::-1]
for j in range(n):
    for i in range(len(lst)):
        ans += lst[i][j]
print(ans)
n, k = map(int, input().split())
p = 2
lst = []
s1 = set()
while True:
    for i in range(p, n+1):
        if i % p == 0 and i not in s1:
            lst.append(i)
            s1.add(i)
    p += 1
    if len(s1) == n-1:
        break
print(lst[k-1])
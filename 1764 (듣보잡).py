n, m = map(int, input().split())

s1 = set()
s2 = set()
for i in range(n):
    s1.add(input())
for i in range(m):
    s2.add(input())

lst = list(s1 & s2)
print(len(lst))
lst.sort()

for i in range(len(lst)):
    print(lst[i])

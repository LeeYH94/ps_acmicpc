n = int(input())
lst = list(map(int, input().split()))
lst.sort()
total = 0
for i in range(1, n+1):
    for j in range(i):
        total += lst[j]
print(total)
n = int(input())
lst = list(map(int, input().split()))
total = 0
for i in range(0, n):
    if lst[i] != i + 1:
        total += 1
print(total)

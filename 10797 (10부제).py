n = int(input())
lst = list(map(int, input().split()))

result = 0
for i in range(len(lst)):
    if lst[i] == n:
        result += 1
print(result)

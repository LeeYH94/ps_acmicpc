n, k = map(int, input().split())
n -= 1
k -= 1
result = 1
if k > 1 and k != 1:
    for i in range(k):
        result *= n
        n -= 1
    for j in range(1, k + 1):
        result //= j
if k == 1:
    result *= n
print(result)
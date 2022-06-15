a, b = map(int, input().split())
result = 1

if a - b < b:
    b = a - b

for i in range(1, b + 1):
    result *= a
    a -= 1
    result //= i

print(result)

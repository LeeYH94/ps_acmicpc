n = int(input())

result = 0
for i in range(n):
    a, b = map(int, input().split())
    result += b % a
print(result)

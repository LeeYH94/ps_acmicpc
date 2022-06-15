import math
a, b = map(int, input().split())
result = 0
for i in range(1, a+1):
    result += int(math.pow(i, b))
    result %= 1000000007

print(result)
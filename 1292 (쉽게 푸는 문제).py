s = []
result = 0
for i in range(1, 100):
    s += [i] * i

a, b = map(int, input().split())
for i in range(a - 1, b):
    result += int(s[i])
print(result)
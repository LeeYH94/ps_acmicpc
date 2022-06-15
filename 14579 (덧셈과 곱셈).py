a, b = map(int, input().split())
ans = 1
for i in range(a, b+1):
    temp = 0
    for j in range(1, i+1):
        temp += j
    ans *= temp
    ans %= 14579
print(ans)
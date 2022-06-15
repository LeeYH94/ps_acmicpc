n = int(input())
ans = 0
for i in range(1, int(n ** (1/2)) + 1):
    ans += 1
print(ans)
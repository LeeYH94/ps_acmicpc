n, m = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0
for i in range(n+1):
    for j in lst:
        if i % j == 0:
            ans += i
            break
print(ans)
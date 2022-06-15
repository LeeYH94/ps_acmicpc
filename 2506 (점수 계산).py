n = int(input())
lst = list(map(int, input().split()))
ans = 0
accum = 0
for i in lst:
    if i == 1:
        accum += 1
        ans += accum
    elif i == 0:
        accum = 0
print(ans)
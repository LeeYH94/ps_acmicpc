a, b, c = map(int, input().split())
ans = 0
cnt = 0
while ans < c:
    ans += a
    cnt += 1
    if cnt % 7 == 0:
        ans += b
print(cnt)
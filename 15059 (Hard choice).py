a, b, c = map(int, input().split())
d, e, f = map(int, input().split())
ans = 0
if d - a > 0:
    ans += d - a
if e - b > 0:
    ans += e - b
if f - c > 0:
    ans += f - c
print(ans)
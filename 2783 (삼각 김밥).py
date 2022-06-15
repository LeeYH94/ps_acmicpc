a, b = map(int, input().split())
ans = 1000 / b * a
for i in range(int(input())):
    a, b = map(int, input().split())
    if 1000 / b * a < ans:
        ans = 1000 / b * a
print("%.2f" % ans)
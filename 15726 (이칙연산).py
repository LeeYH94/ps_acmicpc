a, b, c = map(int, input().split())
ans = a * b / c
if a / b * c > ans:
    print(int(a / b * c))
else:
    print(int(ans))
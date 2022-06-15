def rev(x):
    x = str(x)
    x = x[::-1]
    return int(x)
a, b = map(int, input().split())
result = rev(a) + rev(b)
print(rev(result))

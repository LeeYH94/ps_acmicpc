a, b = map(int, input().split())
c, d = map(int, input().split())
print(c + b if c + b < a + d else a + d)
rate = 0
max_val = 0
for i in range(1,6):
    a, b, c, d = map(int, input().split())
    if a + b + c + d > max_val:
        rate = i
        max_val = a + b + c + d
print("{} {}".format(rate, max_val))

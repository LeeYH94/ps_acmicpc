a, b, c = map(int, input().split())
sec = int(input())
a += sec // 3600
sec = sec % 3600
b += sec // 60
sec = sec % 60
c += sec
if c > 59:
    b += c // 60
    c %= 60
if b > 59:
    a += b // 60
    b %= 60
if a > 23:
    a %= 24
print("{} {} {}".format(a, b, c))

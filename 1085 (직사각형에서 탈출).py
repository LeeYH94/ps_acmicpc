x, y, w, h = input().split()

x = int(x)
y = int(y)
w = int(w)
h = int(h)

xx = w - x
yy = h - y

result = 1000

if xx < result:
    result = xx
if yy < result:
    result = yy
if x < result:
    result = x
if y < result:
    result = y
print(result)

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
s = (x2 - x1)*(y3 - y1) - (y2 - y1)*(x3 - x1)
if s > 0 :
    print(1)
elif s == 0:
    print(0)
else:
    print(-1)
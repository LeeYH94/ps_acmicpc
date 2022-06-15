k = int(input())
d1, d2 = map(int, input().split())
h2 = k**2 - ((d1 - d2)/2)**2
if int(h2) == h2:
    print(int(h2))
else:
    print(h2)
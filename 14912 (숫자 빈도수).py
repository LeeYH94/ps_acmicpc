a, b = map(int, input().split())
s = ''
for i in range(1, a+1):
    s += str(i)
print(s.count(str(b)))
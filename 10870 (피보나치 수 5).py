n = int(input())

a = 0
b = 1
for i in range(n - 1):
    a, b = b, a + b
if n == 0:
    print(0)
else:
    print(b)

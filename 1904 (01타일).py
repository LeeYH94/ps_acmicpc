n = int(input())
a = 1
b = 2

if n >= 3:
    for i in range(3, n + 1):
        a, b = (b % 15746), ((a + b) % 15746)

if n > 1:
    print(b % 15746)
else:
    print(1)

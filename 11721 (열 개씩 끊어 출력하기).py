x = input()

while len(x) % 10 != 0:
    x += ' '
for i in range(10, len(x) +1, 10):
    a = x[i-10 : i]
    print(a.rstrip())

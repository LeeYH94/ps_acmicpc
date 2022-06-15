x = int(input())
a, b = 0, 1
sum = 1
for i in range(x - 1):
    a, b = b, a + b
    if i % 2 != 0:
        sum += b
if x == 1:
    print(1)
else:
    print(sum % 1000000007)
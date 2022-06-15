b = [0] * 300001

n = int(input())
pmsum = 0
a = list(map(int, input().split()))
for i in range(len(a)):
    if i % 2 == 0:
        pmsum += a[i]
    else:
        pmsum -= a[i]

for k in range(n):
    n1 = (k + 1) if k % 2 == 0 else -(k + 1)
    n2 = a[k]
    b[0] += (n1 * n2)

for i in range(1, n):
    if n % 2 == 0 and i > 1:
        pmsum *= -1
    elif i > 1:
        pmsum = -pmsum + 2 * a[i - 2]
    b[i] = pmsum + (-n * a[i - 1] if n % 2 == 0 else n * a[i - 1]) - b[i - 1]

for i in range(n):
    print(b[i], end = ' ')

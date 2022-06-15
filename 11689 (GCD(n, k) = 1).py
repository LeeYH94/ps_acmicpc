n = int(input())
result = n
i = 2
while i * i <= n:
    if n % i == 0:
        result  = result * (i - 1) // i
    while n % i == 0:
        n = n // i
    i += 1
if n != 1:
    result = result * (n - 1) // n
print(result)

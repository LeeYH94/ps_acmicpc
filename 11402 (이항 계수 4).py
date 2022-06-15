n, k, m = map(int, input().split())

result = 1
while n or k:
    temp_n = n % m
    temp_k = k % m
    if temp_n < temp_k:
        print(0)
        exit()
    if temp_n - temp_k < temp_k:
        temp_k = temp_n - temp_k

    for i in range(1, temp_k + 1):
        result *= temp_n
        temp_n -= 1
        result //= i
    n = int(n // m)
    k = int(k // m)
    result %= m
print(result)
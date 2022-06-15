n = int(input())
ans = 0
for i in range(1, int(n**(1/2)) + 1):
    if n % i == 0:
        if i * i == n:
            ans += i
        else:
            ans += i + n // i
print(ans * 5 - 24)
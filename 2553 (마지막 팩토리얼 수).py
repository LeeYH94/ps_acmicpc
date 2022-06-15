n = int(input())
ans = 1
for i in range(1, n+1):
    ans *= i
    ans %= 100000000000000
    while ans % 5 == 0:
        ans //= 10
print(str(ans)[-1])
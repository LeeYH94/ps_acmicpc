n = int(input())
cnt = 1
while 1:
    if n == 1:
        break
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
    cnt += 1
print(cnt)
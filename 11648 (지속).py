n = input()
cnt = 0
while len(n) != 1:
    ans = 1
    for i in n:
        ans *= int(i)
    n = str(ans)
    cnt += 1
print(cnt)
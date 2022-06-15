a, b = input().split()
ans = 100000
for i in range(len(b) - len(a) + 1):
    cnt = 0
    for j in range(len(a)):
        if a[j] != b[i+j]:
            cnt += 1
    if cnt < ans:
        ans = cnt
print(ans)
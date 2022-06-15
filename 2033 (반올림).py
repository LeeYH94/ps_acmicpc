s = list(input())
ans = ''
for i in range(len(s) - 1, 0, -1):
    if int(s[i]) >= 5:
        s[i - 1] = str(int(s[i-1]) + 1)
    ans = ans + '0'
    s[i] = '0'
ans = s[0] + ans
print(ans)
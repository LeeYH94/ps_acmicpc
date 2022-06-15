import sys
s = sys.stdin.readline()
cnt_1 = 0
cnt_0 = 0
for i in range(1, len(s)):
    if s[i] != s[i-1]:
        if s[i-1] == '1':
            cnt_1 += 1
        else:
            cnt_0 += 1
print(cnt_1 if cnt_1 < cnt_0 else cnt_0)
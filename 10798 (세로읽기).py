lst = [''] * 15
for i in range(5):
    s = input()
    for j in range(len(s)):
        lst[j] += s[j]
for i in lst:
    print(i, end='')

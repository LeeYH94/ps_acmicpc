lst = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']
s = input()
s1 = ''
for i in range(len(s)):
    if s[i] not in lst:
        s1 += s[i]
print(s1)
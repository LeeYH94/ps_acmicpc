n = int(input())

lst1 = list(input())
lst2 = lst1[::-1]
s = ''
result = ''
if lst1.count('?') == len(lst1):
    result = "a" * len(lst1)
else:
    for i in range(len(lst1)):
        if lst1[i] == '?':
            s += lst2[i]
        else:
            s += lst1[i]
    for i in range(len(s)):
        if s[i] == '?':
            result += 'a'
        else:
            result += s[i]
print(result)
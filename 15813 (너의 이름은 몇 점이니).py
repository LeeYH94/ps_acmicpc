n = input()
s = input()
result = 0
for i in range(len(s)):
    result += ord(s[i]) - 64
print(result)

s = input()
result = ''
for i in s:
    if ord(i) < 97:
        result += i.lower()
    else:
        result += i.upper()
print(result)

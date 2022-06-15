n = int(input())
s = bin(n)
s = s[2:]
s = '0b' + s[::-1]
print(int(s, 2))
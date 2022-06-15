s1 = input()
key = ord(s1[0]) - ord('C')
s2 = ''
for i in range(len(s1)):
    s2 += chr(ord(s1[i]) ^ key)
s3 = ''
key = ord(s2[0]) - ord('C')
for i in range(len(s2)):
    s3 += chr(ord(s2[i]) ^ key)
print(s3)
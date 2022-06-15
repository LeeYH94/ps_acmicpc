import hashlib
str = input()
result = hashlib.sha1(str.encode()).hexdigest()
print(result)
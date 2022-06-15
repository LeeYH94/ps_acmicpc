import hashlib
str = input()
result = hashlib.sha512(str.encode()).hexdigest()
print(result)
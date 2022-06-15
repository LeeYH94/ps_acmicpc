import hashlib
str = input()
result = hashlib.sha224(str.encode()).hexdigest()
print(result)
import hashlib
str = input()
result = hashlib.sha256(str.encode()).hexdigest()
print(result)
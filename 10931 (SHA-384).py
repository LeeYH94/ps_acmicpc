import hashlib
str = input()
result = hashlib.sha384(str.encode()).hexdigest()
print(result)
import base64

s = input()
b = s.encode("UTF-8")
e = base64.b64encode(b)
e = e.decode("UTF-8")
print(e)

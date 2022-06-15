a, b = input().split()

a = int(a)
b = int(b)

if b < 45:
   if a != 0:
      a -= 1
      b = b + 15
   elif a == 0:
      a = 23
      b = b + 15
else :
   b -= 45

print(str(a) + ' ' + str(b))

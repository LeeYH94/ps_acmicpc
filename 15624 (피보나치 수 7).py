def fibonacci(n):
   if n < 2:
      return n
   
   a, b = 0, 1
   for i in range(n-1):
      a,b = b, a+b
      if b > 1000000007:
         b = b % 1000000007
   return b

x = int(input())
print(fibonacci(x))

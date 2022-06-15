lst= [0, 1, 2, 4, 0, 0, 0, 0, 0, 0, 0]

n = int(input())

def plus(n):
   x = lst[n-3] + lst[n-2] + lst[n-1]
   lst[n] = x

for i in range(n):
   num = int(input())
   if num > 3:
      for j in range(4, num + 1):
         plus(j)

   print(lst[num])

n = int(input())

for i in range(n):
   br = input()
   l_br = 0
   r_br = 0

   for i in range(len(br)):
      if br[i] == '(':
         l_br += 1
      elif br[i] == ')':
         r_br += 1
         
      if l_br < r_br:
         print('NO')
         break
   if l_br == r_br:
      print('YES')
   elif l_br > r_br:
      print('NO')

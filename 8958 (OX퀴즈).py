n = int(input())

for i in range(n):
   ox = input()

   prev = 'X'
   accum = 0
   score = 0

   for i in range(len(ox)):
      if ox[i] == 'O':
         accum += 1
         score += accum
         prev = 'O'

      elif ox[i] == 'X':
         accum = 0
         prev = 'X'
   print(score)

n = int(input())
for i in range(n):
   a,b = input().split()
   a = int(a)
   answer = ''
   for i in range(len(b)):
      answer += b[i] * a
   print(answer)

n = int(input())
lst = []
answer = 0

lst = input().split()

for i in range(n):
   #i = 0 1 2 3 4 ... n-1
   wrong_num = 0
   for j in range(1, int(lst[i])):
      #j = 1 2 3 4 5 ... 
      if int(lst[i]) % j == 0:
         wrong_num += 1
      
   if wrong_num == 1 and int(lst[i]) != 1:
      answer += 1
print(answer)

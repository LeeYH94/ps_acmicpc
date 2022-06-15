lst =[]
result = 0
for i in range(9):
   n = int(input())
   lst.append(n)
   result += n

for i in lst:
   for j in lst:
      if i != j:
         if result - (i + j) == 100:
            lst.remove(i)
            lst.remove(j)
            lst.sort()
            for i in lst: print(i)
            exit();
            

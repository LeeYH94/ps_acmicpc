lst = []
for i in range(10):
   n = int(input())
   lst.append(n % 42)
   set1 = set(lst)
print(len(set1))

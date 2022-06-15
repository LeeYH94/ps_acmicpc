n = int(input())

for i in range(n):
   a, b = input().split()
   a = int(a)
   b = int(b)

   print("Case #{}: {} + {} = {}".format(i+1, a, b, a + b))

n = int(input())

lst = input().split()

max_num = -1000000
min_num = 1000000

for i in range(n):
   if int(lst[i]) > max_num:
      max_num = int(lst[i])
   if int(lst[i]) < min_num:
      min_num = int(lst[i])
print('{} {}'.format(min_num, max_num))

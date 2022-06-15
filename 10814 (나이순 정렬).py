from operator import itemgetter
n = int(input())

lst = []
for i in range(n):
    a, b = input().split()
    a = int(a)
    temp_lst = [a, b]
    lst.append(temp_lst)
    
lst.sort(key = itemgetter(0))
for i in range(n):
    print(str(lst[i][0]) + " " + lst[i][1])

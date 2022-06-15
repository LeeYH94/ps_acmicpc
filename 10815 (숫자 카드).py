a = input()
lst1 = list(map(int, input().split()))
b = input()
lst2 = list(map(int, input().split()))
s1 = set(lst1) & set(lst2)

for i in lst2:
    if i in s1:
        print(1, end = ' ')
    else:
        print(0, end = ' ')

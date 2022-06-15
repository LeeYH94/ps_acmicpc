n1 = int(input())
lst1 = list(map(int, input().split()))
n2 = int(input())
lst2 = list(map(int, input().split()))
s1 = set(lst2) - set(lst1)

for i in lst2:
    if i not in s1:
        print(1)
    else:
        print(0)

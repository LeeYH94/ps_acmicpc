n = int(input())
lst = list(map(int, input().split()))
s1 = set(lst)
print(len(lst) - len(s1))

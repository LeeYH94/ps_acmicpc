n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
if lst[2] - lst[1] == lst[1] - lst[0]:
    print(lst[-1] + lst[1] - lst[0])
else:
    print(lst[-1] * (lst[1] // lst[0]))
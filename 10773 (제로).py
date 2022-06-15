n = int(input())
lst = []

for i in range(n):
    a = int(input())
    if a == 0:
        lst.pop()
    else:
        lst.append(a)

result = 0
for i in range(len(lst)):
    result += lst[i]
print(result)

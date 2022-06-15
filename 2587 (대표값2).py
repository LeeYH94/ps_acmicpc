lst = [0] * 5
total = 0
for i in range(5):
    lst[i] = int(input())
    total += lst[i]
lst.sort()
print(total // 5)
print(lst[2])

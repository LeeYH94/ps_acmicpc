lst = [0]
for i in range(1, 101):
    lst.append(lst[i-1] + i**2)
while 1:
    n = int(input())
    if n == 0:
        break
    print(lst[n])
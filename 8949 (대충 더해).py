a, b = input().split()
a = a[::-1] + "000000000000"
b = b[::-1] + "000000000000"
lst = []
for i in range(10):
    lst.append(int(a[i]) + int(b[i]))
lst.reverse()
print(lst)
s = ""
for i in range(len(lst)):
    if lst[i] != 0:
        s += str(lst[i])

print(s)
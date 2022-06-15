lst1 = []
lst2 = []
ans = 0
for i in range(8):
    n = int(input())
    lst1.append(n)
    lst2.append(n)
    ans += n

lst2.sort()
s = ""
for i in range(len(lst1)):
    if lst1[i] == lst2[0] or lst1[i] == lst2[1] or lst1[i] == lst2[2]:
        ans -= lst1[i]
    else:
        s += str(i + 1)
print(ans)
for i in range(5):
    if i == 4:
        print(s[i])
    else:
        print(s[i], end=' ')
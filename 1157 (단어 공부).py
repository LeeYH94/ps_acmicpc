s = input().upper()
s1 = set(s)

count = 0
temp = ""
lst = []
for i in s1:
    if s.count(i) >= count:
        lst.append(s.count(i))
        count = s.count(i)
        temp = i
lst.sort(reverse = True)

if len(lst) > 1:
    if lst[0] == lst[1]:
        print('?')
    else:
        print(temp)
else:
    print(temp)
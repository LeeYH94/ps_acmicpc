pit = 0
#people_in_train
lst = []
for i in range(4):
    a, b = input().split()
    a = int(a)
    b = int(b)

    pit -= a
    pit += b
    lst.append(pit)
lst.sort(reverse = True)
print(lst[0])

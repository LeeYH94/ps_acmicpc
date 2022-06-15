lst = []
n = int(input())
for i in range(n):
    lst.append(int(input()))
ifTrue = True
for i in range(1, lst[-1] + 1):
    if i not in lst:
        print(i)
        ifTrue = False
if ifTrue:
    print('good job')
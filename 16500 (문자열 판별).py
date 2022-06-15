s1 = input()
n = int(input())
for i in range(n):
    s2 = input()
    ifTrue = False
    while s2 in s1:
        s1 = s1.replace(s2, '')
        ifTrue = True
    if ~ifTrue:
        print(0)
        exit()
if len(s1) == 0:
    print(1)
else:
    print(0)
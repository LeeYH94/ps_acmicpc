import copy
cnt = 1
for _ in range(int(input())):
    n = int(input())
    lst1 = list(map(int, input().split()))
    while len(lst1) != 2:
        lst2 = copy.deepcopy(lst1)
        lst2.reverse()
        temp = []
        if len(lst2) % 2 != 0:
            for i in range(len(lst1)//2 + 1):
                temp.append(lst1[i] + lst2[i])
        else:
            for i in range(len(lst1)//2):
                temp.append(lst1[i] + lst2[i])
        lst1 = temp
    print("Case #{}:".format(cnt), end=" ")
    if lst1[0] > lst1[1]:
        print("Alice")
    else:
        print("Bob")
    cnt += 1
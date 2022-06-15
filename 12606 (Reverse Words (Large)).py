cnt = 1
for _ in range(int(input())):
    lst = list(input().split())
    lst.reverse()
    print("Case #{}:".format(cnt), end=" ")
    for i in lst:
        print(i, end=' ')
    print()
    cnt += 1

n = input()
lst = list(map(int, input().split()))
for i in lst:
    count = 0
    for j in range(1, i):
        if i % j == 0:
            count += j
    if count == i:
        print("Perfect")
    elif count < i:
        print("Deficient")
    else:
        print("Abundant")

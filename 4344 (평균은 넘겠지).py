n = int(input())

for i in range(n):
    mean = 0
    rate = 0
    lst = []
    lst = input().split()
    for i in range(1, len(lst)):
        mean += int(lst[i])
    mean /= int(lst[0])
    
    for i in range(1, len(lst)):
        if int(lst[i]) > mean:
            rate += 1

    print("%0.3f%%" %(rate / (len(lst) - 1) * 100))

i = 1
while 1:
    n = int(input())
    if n == 0:
        break
    if n % 2 == 0:
        print("{}. even {}".format(i, n//2))
    else:
        print("{}. odd {}".format(i, n//2))
    i += 1
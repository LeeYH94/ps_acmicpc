n = int(input())
while n != 1:
    if n % 2 != 0:
        print(0)
        exit()
    n /= 2
print(1)
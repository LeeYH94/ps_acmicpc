mon = int(input())
day = int(input())

if mon == 1:
    print("Before")
elif mon == 2:
    if day == 18:
        print("Special")
    elif day < 18:
        print("Before")
    else:
        print("After")
else:
    print("After")

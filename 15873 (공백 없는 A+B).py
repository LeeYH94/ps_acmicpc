s = input()
if len(s) == 2:
    print(int(s[0]) + int(s[1]))
elif len(s) == 4:
    print(20)
else:
    if int(s[-1]) == 0:
        print(int(s[0]) + 10)
    else:
        print(10 + int(s[-1]))

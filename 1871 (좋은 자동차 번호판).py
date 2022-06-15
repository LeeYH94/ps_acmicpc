for _ in range(int(input())):
    s = input()
    num1 = (ord(s[0])-65) * 26 ** 2 + (ord(s[1])-65) * 26 + (ord(s[2])-65)
    num2 = int(s[4:])
    if abs(num1 - num2) <= 100:
        print('nice')
    else:
        print('not nice')
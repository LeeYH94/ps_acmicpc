for _ in range(int(input())):
    s = input()
    k = s.lower()
    num_g = 0
    num_b = 0
    for i in k:
        if i == 'g':
            num_g += 1
        elif i == 'b':
            num_b += 1
    if num_g > num_b:
        print("{} is GOOD".format(s))
    elif num_g < num_b:
        print("{} is A BADDY".format(s))
    else:
        print("{} is NEUTRAL".format(s))
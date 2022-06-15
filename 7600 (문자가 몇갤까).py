while 1:
    s = input()
    if s == '#':
        break
    s = s.lower()
    result = 0
    for i in range(97, 123):
        if s.count(chr(i)) > 0:
            result += 1
    print(result)

        #range(97, 123)

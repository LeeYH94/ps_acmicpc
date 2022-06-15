for _ in range(int(input())):
    s = input()
    s = s.lower()
    s2 = set()
    for i in range(len(s)):
        s2.add(s[i])
    s1 = set(map(chr, range(97, 123)))
    lst = []
    if len(s1 - s2) == 0:
        print("pangram")
    else:
        lst = list(s1 - s2)
        lst = sorted(lst)
        result = ''
        for i in lst:
            result += i
        print("missing {}".format(result))


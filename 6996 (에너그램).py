for _ in range(int(input())):
    a, b = input().split()
    lst1 = sorted(list(a))
    lst2 = sorted(list(b))
    if lst1 == lst2:
        print("{} & {} are anagrams.".format(a, b))
    else:
        print("{} & {} are NOT anagrams.".format(a, b))
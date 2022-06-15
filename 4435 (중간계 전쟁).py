for k in range(int(input())):
    lst1 = [1, 2, 3, 3, 4, 10]
    lst2 = [1, 2, 2, 2, 3, 5, 10]
    lst_g = list(map(int, input().split()))
    lst_s = list(map(int, input().split()))
    gan = 0
    sau = 0
    for i in range(len(lst_g)):
        gan += lst1[i] * lst_g[i]
    for i in range(len(lst_s)):
        sau += lst2[i] * lst_s[i]
    if gan > sau:
        print("Battle {}: Good triumphs over Evil".format(k+1))
    elif gan < sau:
        print("Battle {}: Evil eradicates all trace of Good".format(k+1))
    else:
        print("Battle {}: No victor on this battle field".format(k+1))


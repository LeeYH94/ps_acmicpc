while 1:
    s = input()
    if s == "#":
        break
    s1 = ''
    for i in range(len(s)):
        if s[i] == " ":
            s1 += "%20"
        elif s[i] == "!":
            s1 += "%21"
        elif s[i] == "$":
            s1 += "%24"
        elif s[i] == "%":
            s1 += "%25"
        elif s[i] == "(":
            s1 += "%28"
        elif s[i] == ")":
            s1 += "%29"
        elif s[i] == "*":
            s1 += "%2a"
        else:
            s1 += s[i]
    print(s1)
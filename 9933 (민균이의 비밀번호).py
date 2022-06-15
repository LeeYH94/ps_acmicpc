s1 = set()
for _ in range(int(input())):
    s = input()
    if s[::-1] in s1:
        print(str(len(s)) + " " + s[len(s)//2])
    elif s == s[::-1]:
        print(str(len(s)) + " " + s[len(s)//2])
    s1.add(s)

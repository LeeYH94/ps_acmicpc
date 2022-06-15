for _ in range(int(input())):
    s = input()
    s = s.lower()
    if s == s[::-1]:
        print("Yes")
    else:
        print("No")
for _ in range(int(input())):
    n1 = input()
    n2 = n1[::-1]

    total = str(int(n1) + int(n2))
    if total == total[::-1]:
        print("YES")
    else:
        print("NO")

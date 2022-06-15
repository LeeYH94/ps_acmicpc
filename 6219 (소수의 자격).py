import sys
s1 = set([])
for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())

    for i in range(2, n + 1):
        if n % i ** 2 == 0:
            n = n // (i ** 2)
            continue
        while n % i == 0:
            if i in s1:
                s1.remove(i)
            else:
                s1.add(i)
            n = n // i
        if n == 2:
            s1.add(2)
            break
        if n == 1:
            break
    if len(s1) == 0:
        print("DA")
        s1 = set([])
    else:
        print("NE")
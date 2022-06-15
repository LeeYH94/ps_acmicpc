for _ in range(int(input())):
    a, b = map(int, input().split())
    s = input()
    ans = ''
    for i in s:
        ans += chr((a * (ord(i) - 65) + b) % 26 + 65)
    print(ans)
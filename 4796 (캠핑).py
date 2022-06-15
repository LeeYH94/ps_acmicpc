import sys
case = 1
while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if not a and not b and not c:
        break
    print("Case {}:".format(case), end=" ")
    ans = a * (c//b)
    if c % b < a:
        ans += c % b
    else:
        ans += a
    print(ans)
    case += 1
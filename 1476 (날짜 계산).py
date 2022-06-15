e, s, m = map(int, input().split())

result = 1
while 1:
    if e == (result % 15) and s == (result % 28) and m == (result % 19):
        print(result)
        break
    result += 1

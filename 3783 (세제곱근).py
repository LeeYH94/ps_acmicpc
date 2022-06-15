import decimal
for _ in range(int(input())):
    n = int(input())
    s = decimal.Decimal(str(n ** (1.0 / 3.0)))
    s = '%.11f' % s
    print(s[:-1])
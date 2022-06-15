num = int(input())
while 1:
    s = input()
    if s == '=':
        break
    temp = int(input())
    if s == '+':
        num += temp
    elif s == '-':
        num -= temp
    elif s == '*':
        num *= temp
    elif s == '/':
        num //= temp
print(num)
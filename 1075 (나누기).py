s = input()
s = int(s[:-2] + "00")
n = int(input())
while True:
    if s % n == 0:
        print(str(s)[-2:])
        break
    else:
        s += 1
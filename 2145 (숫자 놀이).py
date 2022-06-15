def cal(n):
    n = str(n)
    if len(n) == 1:
        return n
    else:
        result = 0
        for i in range(len(n)):
            result += int(n[i])
        return cal(result)
while 1:
    num = int(input())
    if num == 0:
        break
    print(cal(num))
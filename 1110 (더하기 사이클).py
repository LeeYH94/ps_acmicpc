n = input()
times = 0

def cycle(x):
    x = str(x)
    if int(x) < 10:
        x = '0' + x
    num = str(int(x[0]) + int(x[1]))
    if int(num) < 10:
        num = '0' + num
    
    x = x[1] + num[1]
    global times
    times += 1
    return int(x)

a = cycle(n)
while str(n) != str(a):
    a = cycle(a)
print(times)

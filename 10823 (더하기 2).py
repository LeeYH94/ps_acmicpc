s = ''
ans = 0
while 1:
    try:
        s += input()
    except EOFError:
        break
lst = list(map(int, s.split(',')))
for i in lst:
    ans += i
print(ans)
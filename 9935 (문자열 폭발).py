s = input()
bomb = input()
while bomb in s:
    s = s.replace(bomb, '')
if s == '':
    print('FRULA')
else:
    print(s)

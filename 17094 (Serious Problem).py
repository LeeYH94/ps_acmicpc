n = int(input())
s = input()
if s.count('e') > s.count('2'):
    print('e')
elif s.count('2') > s.count('e'):
    print('2')
else:
    print('yee')
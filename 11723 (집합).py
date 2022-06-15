import sys
s1 = set([])
s_all =set([])
for i in range(1, 21):
    s_all.add(i)
for i in range(int(input())):
    s = sys.stdin.readline().rstrip()
    if s[0:3] == 'add':
        s1.add(int(s[4:]))
    elif s[0:3] == 'all':
        s1 = s_all
    elif s[0:5] == 'empty':
        s1.clear()
    elif s[0:5] == 'check':
        if int(s[6:]) in s1:
            print(1)
        else:
            print(0)
    elif s[0:6] == 'remove':
        s1.discard(int(s[7:]))
    elif len(s) > 7:
        if int(s[7:]) in s1:
            s1.discard(int(s[7:]))
        else:
            s1.add(int(s[7:]))

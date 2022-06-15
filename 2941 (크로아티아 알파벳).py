s = input()
count = 0
for i in range(len(s) - 1):
    if s[i] == 'c':
        if s[i + 1]  == '=':
            continue
        elif s[i + 1] == '-':
            continue
        count += 1
    elif s[i] == 'd':
        if s[i + 1] == '-':
            continue
        if i < len(s) - 2:
            if s[i + 1] == 'z' and s[i + 2] == '=':
                continue
        count += 1
    elif s[i] == 'l':
        if s[i + 1] == 'j':
            continue
        count += 1
    elif s[i] == 'n':
        if s[i + 1] == 'j':
            continue
        count += 1
    elif s[i] == 's':
        if s[i + 1] == '=':
            continue
        count += 1
    elif s[i] == 'z':
        if s[i + 1] == '=':
            continue
        count += 1
    else:
        count += 1
print(count + 1)

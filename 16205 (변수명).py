a, b = input().split()
camel = ''
snake = ''
pascal = ''
if a == '1':
    camel = b
    pascal = b[0].upper() + b[1:]
    for i in range(len(b)):
        if 65 <= ord(b[i]) <= 90:
            snake += '_' + b[i].lower()
        else:
            snake += b[i]
elif a == '2':
    snake = b
    camel += b[0]
    temp = 0
    for i in range(1, len(b)):
        if b[i-1] == '_':
            camel += b[i].upper()
            temp = i
        if b[i] == '_' or temp == i:
            continue
        else:
            camel += b[i]
    pascal = camel[0].upper() + camel[1:]
elif a == '3':
    pascal = b
    camel = b[0].lower() + b[1:]
    snake = b[0].lower()
    for i in range(1, len(b)):
        if 65 <= ord(b[i]) <= 90:
            snake += '_' + b[i].lower()
        else:
            snake += b[i]

print(camel)
print(snake)
print(pascal)
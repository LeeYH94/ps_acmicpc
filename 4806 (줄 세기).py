line = 0
while 1:
    try:
        s = input()
        line += 1
    except EOFError:
        break
print(line)

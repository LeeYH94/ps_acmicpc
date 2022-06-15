x = input()
lst = [0] * 26

for i in range(len(x)):
    lst[ord(x[i]) - 97] += 1

for i in range(26):
    print(lst[i], end = ' ')

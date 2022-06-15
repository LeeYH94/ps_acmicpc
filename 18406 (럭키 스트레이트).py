s = input()
temp1 = 0
temp2 = 0
for i in range(len(s)):
    if i < len(s)//2:
        temp1 += int(s[i])
    else:
        temp2 += int(s[i])
if temp1 == temp2:
    print("LUCKY")
else:
    print("READY")
n = input()
lst = [0]
num69 = 0
for i in range(len(n)):
    num = 0
    if n[i] == '6' or n[i] == '9':
        num69 += 1
    else:
        for j in range(len(n)):
            if n[i] == n[j]:
                num += 1
        lst.append(num)
    
lst.sort(reverse = True)

if num69 % 2 != 0:
    num69 = num69 // 2 + 1
else:
    num69 = num69 // 2

print(lst[0] if lst[0] > num69 else num69)
        

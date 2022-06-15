n = int(input())

temp_n = 0
i = 1
reverse = True
while(n > 0):
    temp_n = n
    n -= i
    if i % 2 == 0:
        reverse = False
    else:
        reverse = True
    i += 1
    
if reverse:
    print(str(i - temp_n) + '/' + str(temp_n))    
else:
    print(str(temp_n) + '/' + str(i - temp_n))

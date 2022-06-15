a = int(input())
b = int(input())
c = int(input())

result = a * b * c
    
zero, one, two, three, four, five, six, seven, eight, nine = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 
for i in range(len(str(result))):
    if str(result)[i] == '0':
        zero += 1
    if str(result)[i] == '1':
        one += 1
    if str(result)[i] == '2':
        two += 1
    if str(result)[i] == '3':
        three += 1
    if str(result)[i] == '4':
        four += 1
    if str(result)[i] == '5':
        five += 1
    if str(result)[i] == '6':
        six += 1
    if str(result)[i] == '7':
        seven += 1
    if str(result)[i] == '8':
        eight += 1
    if str(result)[i] == '9':
        nine += 1
        
print(zero)
print(one)
print(two)
print(three)
print(four)
print(five)
print(six)
print(seven)
print(eight)
print(nine)

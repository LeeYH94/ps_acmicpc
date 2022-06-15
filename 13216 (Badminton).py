s = input()
sum_a = 0
sum_b = 0
i = 0
temp_a = 0
temp_b = 0
while i < len(s):
    if s[i] == 'A':
        temp_a += 1
    elif s[i] == 'B':
        temp_b += 1
    if temp_a == 21 or temp_b == 21:
        print("{}-{}".format(temp_a, temp_b))
        if temp_a == 21:
            sum_a += 1
        elif temp_b == 21:
            sum_b += 1
        temp_a = 0
        temp_b = 0
    i += 1
if sum_a == 2:
    print("A")
elif sum_b == 2:
    print("B")
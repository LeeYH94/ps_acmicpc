n = int(input())
sum = n * (n**2 + 1) // 2
lst = []
check = True
for _ in range(n):
    lst.append(list(map(int, input().split())))

temp = []
for i in lst:
    for j in range(n):
        temp.append(i[j])
temp.sort()
s1 = set(temp)
if len(s1) != n**2:
    check = False
if temp[0] < 1 or temp[-1] > n**2:
    check = False

for i in range(n):
    temp_num1 = 0
    temp_num2 = 0
    for j in range(n):
        temp_num1 += lst[i][j]
        temp_num2 += lst[j][i]
    if temp_num2 != sum:
        check = False
    if temp_num1 != sum:
        check = False

temp_num3 = 0
for i in range(n):
    temp_num3 += lst[i][i]
if temp_num3 != sum:
    check = False

# temp_num4 = 0
# for i in range(n-1, 0, -1):
#     for j in range(n):
#         temp_num4 += lst[j][i]
# if temp_num4 != sum:
#     check = False
if check:
    print("TRUE")
else:
    print("FALSE")
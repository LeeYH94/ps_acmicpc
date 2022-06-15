a = int(input())
b = int(input())
result = 0
for i in range(b+1):
    result += int(str(a) + str(0) * i)
print(result)
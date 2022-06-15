n = int(input())

for i in range(n):
    temp_i = i
    x = i
    for j in range(len(str(temp_i))):
        x += i % 10
        i = i // 10
    if n == x:
        print(temp_i)
        break
    if temp_i == n-1:
        print(0)
    

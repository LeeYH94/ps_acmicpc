n = int(input())
n = bin(n)[2:]
n = n[::-1]
result = 0
for i in range(len(n)):
    if n[i] == '1':
        result += 3**i
print(result)
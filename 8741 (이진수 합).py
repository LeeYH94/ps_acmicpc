k = int(input())
n = 2 ** k - 1
sum = n * (n + 1) // 2
print(bin(sum)[2:])
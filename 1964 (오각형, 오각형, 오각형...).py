n = 5
plus = 7
num = int(input())
if num == 1:
    print(5)
    exit()
for i in range(num-1):
    n += plus
    plus += 3
print(n % 45678)
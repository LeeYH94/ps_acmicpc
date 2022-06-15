n = int(input())
count = 0
num = 1
for i in range(0, 1000000000):
    count += 1
    num += i * 6
    if num >= n:
        break
print(count)

n = int(input())
count = 0
for i in range(1, n + 1):
    while i % 5 == 0:
        i = i // 5
        count += 1
print(count)

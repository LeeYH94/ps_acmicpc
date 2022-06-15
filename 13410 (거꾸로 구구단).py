a, b = map(int, input().split())
max_num = 0
for i in range(1, b + 1):
    if max_num < int(str(a * i)[::-1]):
        max_num = int(str(a * i)[::-1])
print(max_num)
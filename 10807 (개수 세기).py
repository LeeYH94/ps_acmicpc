n = input()
lst = list(map(int, input().split()))
num = int(input())
result = 0
for i in lst:
    if i == num:
        result += 1
print(result)

a = input()
s1 = set(map(int, input().split()))
n = int(input())

count = 0
for i in s1:
    if n - i in s1:
        count += 1
print(count//2)
a, b = map(int, input().split())
s1 = set()
count = 0
for _ in range(a):
    s1.add(input())

for _ in range(b):
    s = input()
    if s in s1:
        count += 1
print(count)
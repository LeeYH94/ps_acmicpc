a = int(input())
lst = input().split()
s = ''
for i in lst:
    s += i

for _ in range(int(input())):
    a, b = map(int, input().split())
    temp_s = s[a-1 : b]
    if temp_s == temp_s[::-1]:
        print(1)
    else:
        print(0)
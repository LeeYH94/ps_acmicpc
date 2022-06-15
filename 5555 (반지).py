s = input()
ans = 0
for _ in range(int(input())):
    temp = input() * 2
    if s in temp:
        ans += 1
print(ans)
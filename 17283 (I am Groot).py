root = int(input())
r = int(input())
count = 2
ans = 0
while 1:
    node = root * r // 100
    if node <= 5:
        break
    ans += node * count
    count *= 2
    root = node
print(ans)
n = int(input())
lst = list(map(int, input().split()))
temp = 0
ans = 0
for i in range(1, len(lst)):
    if lst[i] > lst[i-1]:
        temp += lst[i] - lst[i-1]
    else:
        if temp > ans:
            ans = temp
        else:
            temp = 0
print(ans)
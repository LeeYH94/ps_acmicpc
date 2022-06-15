s1 = set(['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili'])
lst = list(input().split())
ans = lst[0][0].upper()
for i in range(1, len(lst)):
    if lst[i] not in s1:
        ans += lst[i][0].upper()
print(ans)
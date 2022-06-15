dict = {}
ans = 0
for i in range(10):
    n = int(input())
    ans += n
    if n not in dict:
        dict[n] = 1
    else:
        dict[n] += 1
lst = sorted(dict.items(), key = lambda x : x[1], reverse = True)
print(ans // 10)
print(lst[0][0])

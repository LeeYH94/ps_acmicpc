a, b = map(int,input().split())
lst = list(map(int, input().split()))

max_val = 0
for i in range(len(lst)):
    for j in range(i + 1 ,len(lst)):
        for k in range(j + 1,len(lst)):
            if lst[i] + lst[j] + lst[k] <= b:
                if lst[i] + lst[j] + lst[k] >= max_val:
                    max_val = lst[i] + lst[j] + lst[k]
print(max_val)

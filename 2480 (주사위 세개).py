lst = [0] * 7
a, b, c = map(int, input().split())
lst[a] += 1
lst[b] += 1
lst[c] += 1

max_idx = 0
print_idx = 1
for i in range(len(lst)):
    if lst[i] == 3:
        print(10000 + i * 1000)
        print_idx = 0
        break
    elif lst[i] == 2:
        print(1000 + i * 100)
        print_idx = 0
        break
    elif lst[i] == 1:
        max_idx = i
if print_idx:
    print(max_idx * 100)

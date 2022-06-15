lst = []
for i in range(1, 350):
    if i * i  < 100000:
        lst.append(i * i)

n = int(input())
trial = 0

while(n > 0):
    temp_n = n
    for i in range(temp_n, 0, -1):
        if lst.count(i) == 1:
            n -= i
            trial += 1
            break
print(trial)

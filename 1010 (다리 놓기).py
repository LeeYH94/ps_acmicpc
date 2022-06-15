num = int(input())

for i in range(num):
    n, m = input().split()
    n = int(n)
    m = int(m)
    result = 1
    facto = 1
    for i in range(n):
        result *= (m - i)
        facto *= (i + 1)
    print(result // facto)

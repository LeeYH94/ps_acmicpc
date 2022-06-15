import math
n = int(input())
n = math.sqrt(n)
if math.floor(n) == n:
    print(math.floor(n))
else:
    print(math.floor(n) + 1)

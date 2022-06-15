import sys

n = int(input())
kilo = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))
ans = 0

for i in range(1, len(cost)):
    if cost[i] > cost[i-1]:
        cost[i] = cost[i-1]

for i in range(len(kilo)):
    ans += kilo[i] * cost[i]
print(ans)
cute = 0
for _ in range(int(input())):
    n = int(input())
    if n == 1:
        cute += 1
    else:
        cute -= 1
if cute > 0:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')

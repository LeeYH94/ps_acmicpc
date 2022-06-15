n = int(input())
if n == 1:
    print("*")
else:
    print(" " * (n-1) + "*")
    k = n
    for i in range(n-2, -1, -1):
        print(" " * i + "*", end="")
        print(" " * ((n-k)*2+1) + "*")
        k -= 1
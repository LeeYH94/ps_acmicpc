test = int(input())
result = ''
for i in range(0, test):
    x, y = input().split()
    x = int(x)
    y = int(y)

    result += str(x + y) + ("\n" if i != test-1 else '')
print(result)

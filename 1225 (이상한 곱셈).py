import sys
a, b = sys.stdin.readline().split()

temp_a = 0
temp_b = 0
for i in range(len(a)):
    temp_a += int(a[i])
for j in range(len(b)):
    temp_b += int(b[j])
print(temp_a * temp_b)
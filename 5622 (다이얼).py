lst = [3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10]

answer = 0
x = input()
for i in range(len(x)):
   answer += lst[ord(x[i]) - 65]
print(answer)

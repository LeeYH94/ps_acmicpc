n = input()
lst = []

for i in range(len(n)):
   lst.append(n[i])

lst.sort(reverse = True)

answer = ''

for i in range(len(n)):
   answer += lst[i]

print(answer)

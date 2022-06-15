science = []
social = []
for i in range(4):
    science.append(int(input()))
for i in range(2):
    social.append(int(input()))
science.sort()
social.sort()
print(science[1] + science[2] + science[3] + social[1])

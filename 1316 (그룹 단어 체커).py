import string
n = int(input())
result = n

for i in range(n):
    alphabet = dict(zip(string.ascii_lowercase, [0]*26))
    prev_alp = ''
    eng = input()
    for i in range(0, len(eng)):
        if eng[i] != prev_alp:
            if alphabet[eng[i]] == 1:
                result -= 1
                break
        prev_alp = eng[i]
        alphabet[eng[i]] = 1

print(result)
    

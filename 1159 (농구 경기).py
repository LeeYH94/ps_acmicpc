import sys
lst = [0 for _ in range(26)]
for _ in range(int(sys.stdin.readline())):
    s = sys.stdin.readline()[0]
    lst[ord(s)-97] += 1

if sorted(lst, reverse=True)[0] < 5:
    print("PREDAJA")
else:
    for i in range(len(lst)):
        if lst[i] >= 5:
            print(chr(i+97), end="")
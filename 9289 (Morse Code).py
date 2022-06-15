morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--',
         '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
case = 1
for _ in range(int(input())):
    lst = list(input().split())
    ans = ''
    for i in lst:
        for j in range(len(morse)):
            if i == morse[j]:
                ans += chr(j+65)
    print("Case {}: {}".format(case, ans))
    case += 1
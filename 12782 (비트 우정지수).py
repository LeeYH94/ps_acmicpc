for _ in range(int(input())):
    a, b = input().split()
    cnt0 = 0
    cnt1 = 0
    cnt2 = abs(a.count('1') - b.count('1'))
    for i in range(len(a)):
        if a[i] == '0' and b[i] == '1':
            cnt0 += 1
        elif a[i] == '1' and b[i] == '0':
            cnt1 += 1
    print(cnt2 + (cnt0 if cnt0 < cnt1 else cnt1))
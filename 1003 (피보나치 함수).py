n = int(input())

lst_zero = [1, 0, 1]
lst_one = [0, 1, 1]

for i in range(3, 41):
    lst_zero.append(lst_zero[i - 2] + lst_zero[i - 1])
    lst_one.append(lst_one[i - 2] + lst_one[i - 1])

for i in range(n):
    num = int(input())
    print(str(lst_zero[num]) + ' ' + str(lst_one[num]))

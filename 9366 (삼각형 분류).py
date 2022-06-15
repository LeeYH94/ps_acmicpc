for i in range(int(input())):
    lst = list(map(int, input().split()))
    lst = sorted(lst)
    if not lst[2] < lst[1] + lst[0]:
        print("Case #{}: invalid!".format(i + 1))
    elif lst[0] == lst[1] and lst[1] == lst[2]:
        print("Case #{}: equilateral".format(i + 1))
    elif lst[0] == lst[1] or lst[1] == lst[2]:
        print("Case #{}: isosceles".format(i + 1))
    else:
        print("Case #{}: scalene".format(i + 1))
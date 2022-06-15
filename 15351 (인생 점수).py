for _ in range(int(input())):
    result = 0
    for i in input():
        if 65 <= ord(i) <= 91:
            result += ord(i) - 64
    if result == 100:
        print("PERFECT LIFE")
    else:
        print(result)

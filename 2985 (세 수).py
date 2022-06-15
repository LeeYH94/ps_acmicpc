a, b, c = map(int, input().split())
if c == a + b:
    print("{}+{}={}".format(a, b, c))
elif c == a - b:
    print("{}-{}={}".format(a, b, c))
elif c == a * b:
    print("{}*{}={}".format(a, b, c))
elif c == a / b:
    print("{}/{}={}".format(a, b, c))
elif a == b + c:
    print("{}={}+{}".format(a, b, c))
elif a == b - c:
    print("{}={}-{}".format(a, b, c))
elif a == b * c:
    print("{}={}*{}".format(a, b, c))
elif a == b / c:
    print("{}={}/{}".format(a, b, c))

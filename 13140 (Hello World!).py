import itertools
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
n = int(input())
p = itertools.permutations(lst, 7)
for i in p:
    d, e, h, l, o, r, w = i
    if h == 0 or w == 0:
        continue
    hello = 10000 * h + 1000 * e + 100 * l + 10 * l + o
    world = 10000 * w + 1000 * o + 100 * r + 10 * l + d
    if n == hello + world:
        print("  {}".format(hello))
        print("+ {}".format(world))
        print("-------")
        if n > 100000:
            print(" {}".format(n))
        else:
            print("  {}".format(n))
        exit()
print("No Answer")
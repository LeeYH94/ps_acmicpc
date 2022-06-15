def solve(a):
    ans = 0
    if len(a) == 0:
        return ans
    else:
        for i in a:
            ans += int(i)
    return ans

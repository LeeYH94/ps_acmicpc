lst1 = list(map(int, input().split()))
lst2 = sorted(lst1)
if lst1 != lst2:
    print("Bad")
else:
    print("Good")
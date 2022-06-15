import sys
test, system = map(int, input().split())
test_case = True
system_case = True
for i in range(test):
    a, b = map(int, sys.stdin.readline().split())
    if a != b:
        test_case = False
for i in range(system):
    a, b = map(int, sys.stdin.readline().split())
    if a != b:
        system_case = False
if test_case and system_case:
    print("Accepted")
elif test_case == False:
    print("Wrong Answer")
elif test_case == True and system_case == False:
    print("Why Wrong!!!")
    

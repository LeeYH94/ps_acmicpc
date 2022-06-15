while 1:
    s = input()
    if s == '.':
        break
    balance = 'yes'
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append('brk')
        elif s[i] == ')':
            if len(stack) == 0:
                balance = 'no'
                break
            if stack[-1] == 'brk':
                stack.pop()
            else:
                balance = 'no'
                break                
        elif s[i] == '[':
            stack.append('sqr_brk')
            
        elif s[i] == ']':
            if len(stack) == 0:
                balance = 'no'
                break
            if stack[-1] == 'sqr_brk':
                stack.pop()
            else:
                balance = 'no'
                break      
    if len(stack) != 0:
        balance = 'no'
    print(balance)


N = int(input())

for i in range(N):
    stack = [] 
    ans =list(input())

    if len(ans)%2 != 0:
        print("NO")
        continue
    
    is_valid = True
    for i in ans: 
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack:
                is_valid = False
                break
            else:
                stack.pop()    
    
    if is_valid and not stack:
        print("YES")
    else:
        print("NO")
N = int(input())

for _ in range(N):
    stack = []
    ans = input().strip()  # 개행 문자 제거
    
    if len(ans) % 2 != 0:
        print("NO")
        continue
    
    is_valid = True
    for char in ans:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:  # 스택이 비어있는지 확인
                is_valid = False
                break
            stack.pop()
    
    if is_valid and not stack:
        print("YES")
    else:
        print("NO")
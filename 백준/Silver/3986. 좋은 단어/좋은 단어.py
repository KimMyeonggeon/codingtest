import sys
input = sys.stdin.readline

N = int(input())
count = 0

for _ in range(N):
    word = input().strip()  # 개행 문자 제거
    if len(word) % 2 != 0:  # 홀수 길이 문자열은 즉시 실패 처리
        continue
    
    stack = []
    for char in word:
        if not stack or stack[-1] != char:
            stack.append(char)
        else:
            stack.pop()
    
    if not stack:
        count += 1

print(count)
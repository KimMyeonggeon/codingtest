import sys
input = sys.stdin.readline

N = int(input())

list = [] 
for i in range(N):
    n = int(input())

    if n == 0:
        list.pop()
    else:
        list.append(n)

print(sum(list))
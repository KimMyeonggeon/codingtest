import sys 
input = sys.stdin.readline

n = int(input())
d= [0] * (n+1)
if n >= 1:
    d[1] = 1
if n >= 2:
    d[2] = 2

    
for j in range(3,n+1):
    d[j] = (d[j-1] + d[j-2]) % 10007
print(d[n])


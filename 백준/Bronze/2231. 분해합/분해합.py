import sys

n = int(sys.stdin.readline())

num =0

for i in range (n+1):
    sum = 0
    for j in str(i):
        sum += int(j)
    if (sum+i == n ):
        num = i 
        break

print(num)


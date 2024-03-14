import sys

n,m = map(int, sys.stdin.readline().split())
l = list(map(int, input().split()))
sum =0
num =0 

for i in range(len(l)):
    for j in range(i+1,len(l)-1):
        for k in range(j+1, len(l)):
            num = l[i]+ l[j] + l[k]
            if( num <= m):
                if(num > sum):
                    sum = num 

print(sum)
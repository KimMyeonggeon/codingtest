l = [['-'] * 100 for _ in range(100)] 
n = int(input())
c=0

for i in range(n):
    x,y= map(int, input().split())
    for p in range(x,x+10):
        for q in range (y, y+10):
            if l[p][q] != '*' : 
                l[p][q] = '*'
                
for i in range(100):
    for j in range(100):
        if l[i][j] == '*':
            c += 1

print(c )
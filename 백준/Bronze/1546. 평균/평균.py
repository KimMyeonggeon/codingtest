n = int(input())
l = list(map(int, input().split()))
sum= 0.0
m= max(l)
for i in range(n):
    sum += l[i]/m *100 

print (float(sum/n))


l =[] 
sum =0 

for i in range (9):
    n = int(input())
    l.append(n)
    sum += n


for i in range(len(l)):
    for j in range(i+1,len(l)):
        if ( l[i]+ l[j] == sum-100 ):
            x= l[i]
            y= l[j]
l.remove(x)
l.remove(y)

for k in range(len(l)):
    print(l[k])
            

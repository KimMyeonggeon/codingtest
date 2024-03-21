i = int(input())


for h in range(i):
    k = int(input())
    n= int(input())
    l = ['0'] * n 
    t = ['0'] * n 
    for i in range (n):
        l[i] = i+1
    t = l [:]

    

    for p in range(k):
        for q in range(n):
            
            if (q== 0):
                
                l[q]= t[q]
            else:
                sum=0
                for j in range(q+1):
                    sum += t[j]
                
                l[q] = sum  
        t = l [:]
        
        if( p == k-1 and q == n-1):
            print(l[q])
    
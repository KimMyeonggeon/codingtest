
n,m= map(int,input().split())

il=[]
count= []

for i in range (n):
    l = input()
    il.append(l)

for i in range(n-7):
    for j in range(m-7):
        # print(il[i][j])
        wc =0
        bc =0
        
        for k in range(i, i+8):
            for p in range (j, j+8):
                if ( (k+p) % 2 == 0 ): 
                    if( il[k][p] != 'B'):
                        bc += 1 
                    if( il[k][p] != 'W'):
                        wc += 1 
                else : 
                    if( il[k][p] != 'W'):
                        bc += 1
                    if( il[k][p] != 'B'):
                        wc += 1 

        count.append(min(wc,bc))
print(min(count))
n = int(input())

c= n
for i in range( n ):
    w = input()
    
    for j in range (0, len(w)-1):
        
        if w[j] == w[j+1] :
            pass
        elif w[j] in w[j+1:]:
            c -= 1
            break
    
print (c)

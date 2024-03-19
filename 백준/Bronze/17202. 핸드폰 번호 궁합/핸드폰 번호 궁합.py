n = input()
m = input()
l=[]

for i in range (len(n)):
    l.append(int( n[i] ))
    l.append(int( m[i] ))

while len(l) != 2:
    sl =[]
    for i in range (len (l)-1):
        if (l[i]+l[i+1] >= 10 ):
            num= (l[i]+l[i+1]) % 10 
            sl.append(num)
        else:
            sl.append( l[i]+l[i+1])
    l = sl[:] 

print(str(l[0])+ str(l[1]))
w= input().upper()

l= list(set(w))
c_l=[]

for i in l:
    c= w.count(i)
    c_l.append(c)

if c_l.count(max(c_l)) > 1 :
    print ('?')
else : 
    print( l[c_l.index(max(c_l))])
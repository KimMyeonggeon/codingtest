a= int(input())
b= int(input())
c= int(input())
l=[]
multi = a * b * c 

for i in str(multi):
    l.append(i)
    

for j in range (10):
    print (l.count('{}'.format(j)))


n = input()
f= int(input())
num= n[:-2]  #앞자리 
m= 0

for i in range(100):
    if (i < 10 ):
        m = str(i).zfill(2)
        
        if (int(num+ m ) % f == 0):  
            print (m)
            break

    else: 
        if (int(num+ str(i)) % f == 0):
            print (i)
            break

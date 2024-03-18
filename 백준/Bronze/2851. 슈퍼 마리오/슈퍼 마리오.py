l =[] 
sum =0 
num =0

for i in range (10):
    n = int(input())
    l.append(n)
    

for i in range(len(l)):
    sum += l[i]
    if ( sum == 100):
        num = sum 
        break
    elif( sum > 100):
        if( 100-num >= sum -100 ):
            num = sum 
            break
    else:
        num = sum

print(num)
n= int(input())

for i in range(n):
    h,w,n = map(int, input().split())
    
    height= n%h
    weight = (n//h)+1

    if (height == 0):
        weight -= 1 
        height = h
    
    print(height*100+ weight)
n= int(input())

for i in range(n):
    a = input()
    sum = 0
    num = 0 

    for j in range(len(a)):
        if (a[j] == 'O'):
            num += 1 
            sum += num 
            
        else :
            num = 0 
            sum += num 
    print(sum)
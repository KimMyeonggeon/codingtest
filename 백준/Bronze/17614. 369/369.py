a = input()
sum = 0
numl = ['3','6','9']


for i in range(1, int(a)+1):
    for j in str(i):
        if ( j in numl):
            sum += 1 

print(sum )

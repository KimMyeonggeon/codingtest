n = int(input())
l =[]


for i in range(n+1):
    if (i == 0):
        num = 0
        l.append(num)
    elif (i == 1 ):
        num = 1 
        l.append(num)
    else: 
        num = l[i-2] + l[i-1]
        l.append(num)

print(l[n])

a = list(map(int, input().split()))

l= [1,2,3,4,5,6,7,8]
r_l = list(reversed(l))

if(a == l):
    print("ascending")
elif(a == r_l):
    print("descending")
else:
    print("mixed")
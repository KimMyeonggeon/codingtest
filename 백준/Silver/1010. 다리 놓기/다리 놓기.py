t = int(input())

for i_ in range (t):

    n,m = map(int, input().split())
    fac =1
    gop =1
    n_r =1

    for i in range(1,m+1):
        fac *= i
    for i in range(1,n+1):
        gop *= i
    for i in range (1,m-n+1):
        n_r *= i
    print(int(fac/(gop*n_r)))
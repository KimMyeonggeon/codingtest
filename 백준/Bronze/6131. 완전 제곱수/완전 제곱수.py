n = int(input())
sum =0

for a in range(1,501):
    for b in range(1,a):
        if((a*a) == (b*b)+n):
            sum += 1
print(sum)
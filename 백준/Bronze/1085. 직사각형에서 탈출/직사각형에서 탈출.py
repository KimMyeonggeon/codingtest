x,y,w,h = map(int,input().split())

min_x=x
min_y=y
min=0

if x> w-x:
    min_x= w-x

if y> h-y:
    min_y= h-y

if min_x >= min_y:
    min= min_y
else:
    min= min_x

print(min)
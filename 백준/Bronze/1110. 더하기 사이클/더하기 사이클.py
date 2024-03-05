num = int(input())
j=0
c=num
while num>=0 and num <=99:
  a= c//10
  b=c%10
  s= (a+b)%10
  c= b*10 + s
  j +=1

  if c == num:
    break
print(j)
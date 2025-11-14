# n=int(input("how many numbers"))
# a,b=0,1
# for i in range(n):
#   print(a)
#   a,b=b, a +  b

a=0
b=1
for i in range(0,11):
  c=a+b
  b=a
  a=c
  print(c)  

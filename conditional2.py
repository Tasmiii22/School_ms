# a=10
# b=25
# c=15
# if(a>b and a>c):
#   print(a,"Is greater")
# elif(b>a and b>c):
#   print(b,"Is greater")
# elif(c>a and b<c):
#   print(b,"Is greater")

# else:
#      print("Numbers are equal")

# year=int(input("Enter year"))
# if(year%400==0 and year%100!=0):
#   print("leap year")
# elif(year%4==0):
#    print("Not a leap year")
# else:
#   print("Not a leap year")

# num=[1,2,3,4,5,6,3,7]
# n=[]
# for i in num:
#   if i not in n:
#     n.append(i)
# print(n)

# num=1245
# sum=0
# while num>0:
#   sum=sum+num%10
#   num=num//10
# print(sum)

# tuple=(1,2,3,4)
# list=(list(tuple))
# print(list)
# list.append(5)
# print(list)
# print(type(list))


for i in range(0,11):
  for k in range(i):
    print("*",end=" ")
  for p in range(i-1):
      print("* ",end=" ")
  print( )

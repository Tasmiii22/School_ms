
# #function wiith default parameters
# def fun(a,b=7):
#   print(a-b)
# fun(9)

# #function wiith positional parameters
# def fun1(a,b):
#   print(a*b)
# fun1(a=3,b=3)

from functools import reduce


nums=[1,2,3,4,5,6,7,8,9,10]
def even(a):
  return a%2==0
output=list(filter(even,nums))
print(output)
#higher Order fUNCTION
print(list(filter(lambda x:x%2==0,nums)))

def mul(n):
  return n*4
result=list(map(lambda x:x*4,nums))
print(result)

# def sum(a,b):
#   return a+b
# result1=reduce(sum,result)

# print(result1)
# print(reduce(lambda a,b:a*b,result))


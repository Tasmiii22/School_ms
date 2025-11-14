#Generators
import sys

# def my_list():
#   for i in range(11):
#     yield i
    
# result=my_list()
# print(next(result))
# print(next(result))
# print(next(result))
# print(list(result))
# print(sys.getsizeof(result))

# normal=[i for i in range(11)]
# print(sys.getsizeof(normal))


def squares(n):
  for i in range(1,n+1):
    yield i*i
result1=squares(11)
print(next(result1))
print(next(result1))
print(next(result1))
print(next(result1))
print(list(result1))


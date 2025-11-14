# def func(n):
#   print(n,"is great")

# def callName(func):
#   func("Tasmiya")

# callName(func)

# def num(a,b):
#   print(a+b)
# def call(num):
#   num(3,4)
# call(num)

# def decoration(org_fun):

#   def inner_func():
#     print("First calling the function")
#     org_fun()
#     print("after caling this function")
#   return inner_func()
# def org_fun():
#   print(" Hello python decorators")
# res=decoration(org_fun)
# res()

def add(func):
  def andar(a,b):
    print(a+b)
    func(a,b)
  return andar

@add  #inherits the properties of add function
def tasmiya(a,b):
    print("After calculating")

tasmiya(17,22)






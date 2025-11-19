# # def num(n):
# #   if(n==0):
# #     return
# #   num(n-1)
# #   print(n)
# # num(5)

# def num(n):
#   if(n==11):
#     return
#   num(n+1)
#   print(n)
# num(5)

# def fact(n):
#   if n==0:
#     return 1
#   return n*fact(n-1) 
# print(f"Factorial is:  {fact(5)}")

# def sum(n):
#   if n==0:
#     return 0
#   return n+sum(n-1)
# print(sum(8))

# def rev(str):
#   if len(str)==0:
#     return str
#   return rev(str[1:])+str[0]
# print(rev("Faizan"))
# print(rev("zoya"))
  
# def subsets(numbers):
#     result = []

#     def fasttrack(start, current):
#         result.append(current[:])
        
#         for i in range(start, len(numbers)):
#             current.append(numbers[i])
#             fasttrack(i + 1, current)
#             current.pop()

#     fasttrack(0, [])
#     return result

# print(subsets([1, 2, 3,4]))

#Lambdaa Function
a=lambda x:x+x
print(a(12))

evenodd=lambda n:"even" if n%2==0 else"odd"
print(evenodd(246))


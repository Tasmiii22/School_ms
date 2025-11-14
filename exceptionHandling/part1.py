# try:
#   a=10/3
#   # print(a)
# except ZeroDivisionError:
#   print("Error:Cannot divide by 0")
try:

   n1=int(input("Enter number: "))
   result=10/n1
   print(result)
except ZeroDivisionError:
   print("cannot divide by zero")
except ValueError:
   print("Invalid Input")

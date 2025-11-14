# try:
#   f=open("data1.txt","r")
# except FileNotFoundError:
#   print("File cannot be found")
# else:
#   print("file is Opened Successfully")
# finally:
#   print("Executioin complete")

age=int(input("Enter number: "))
if age<0:
  raise ValueError("Age cannot be negative")
else:
  print("given age is valid")
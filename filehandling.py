
import os

#File handling

# f=open("myfile.txt","w")
# f.write("Hello this is first line of code\n")
# f.write("Hello this is second line of code\n")


# f.close()
   
# f=open("myfile.txt","r")
# c=f.read()
# print(c)
# f.close()

# f=open("myfile.txt","r")
# lines=f.readlines()
# for l in lines:
#   print(l.strip())
# f.close()

# f=open("myfile.txt","r")
# l=f.readline()
# # print(l.strip())
# while l:
#   print(l.strip())
#   l=f.readline()
# f.close()

with open("data.txt","w")as f:
  f.write("Data inserted")

# with open("data.txt","r")as r:
#   print(r.readlines())

# with open("data.txt","r+")as s:
#   print(s.read())
#   print(s.write("\nData inserted2"))
#   print(s.read())

# os.remove("thursday.txt")

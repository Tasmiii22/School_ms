#hollowGram
n=5
for i in range(n):
  for j in range(9):
    if(i==0 or i==n-1 or j==0 or j==9-1):
      print("*",end=" ")
    else:
      print(".",end=" ")
  print()
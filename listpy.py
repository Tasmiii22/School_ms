l=[1,2,2,2,3,3,3,4,4,4]
f={}
for i in l:
  if i in f:
    f[i]+=1
  else:
    f[i]=1
print("number occuring ",f[i],"times")
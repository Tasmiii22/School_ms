l1=[1,1,1,2,2,3,4,4,5,6,7,7]
count={}
for i in l1:
  if i in count:
    count[i]+=1
  else:
    count[i]=1
  
  if count[i]>1:
    print(i," ",count[i],"times")
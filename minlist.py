mylist=[21,34,56,3,78,89,34,65]
max_num=mylist[0]
for i in range(1,len(mylist)):
  if(mylist[i]<max_num):
    max_num=mylist[i]
     
print(max_num,"Is min in list")
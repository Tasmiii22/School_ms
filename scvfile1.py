import csv
import pandas  as pd

# data=[
#   ["Name","Age","City"],
#   ["Tasmiya",21,"Pune"],
#   ["Zoya",22,"Pune"],
#   ["Tehrin",18,"Pune"],
#   ["Mufiz",20,"Pune"]
# ]

# with open("person1.csv","w", newline="")as f:
#   save=csv.writer(f)
#   save.writerows(data)

# with open("person1.csv","r")as s:
#   see=csv.reader(s)
#   for i in see:
#     print(i)

# with open("person1.csv","a")as a:
#   ap=csv.writer(a)
#   d1=[["Ali",1,"Mumbai"],
#       ["abc",34,"rcr"]
#   ]
#   ap.writerows(d1)

data=[
  {"Name":"Rohan","Age":21,"City":"Mumbai"},
  {"Name":"Sana","Age":22,"City":"Mumbaiieee"}
]
# with open("person2.csv","w")as f:
#   nameOffeilds=["Name","Age","City"]
#   see=csv.DictWriter(f,fieldnames=nameOffeilds)
#   see.writeheader()

#   see.writerows(data)

result=pd.read_csv("person2.csv")
print(result)





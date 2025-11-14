import json as js
data={
  "name":"Sana",
  "Age":22,
  "skills":["Python","Java","C"],
  "City":"Punee"
}

with open("data2.json","w")as f:
  js.dump(data,f,indent=9)


# with open("data2.json","r")as f:
#   print(js.load(f))
dict={"Username":"Tasmiya","Role":"Developer","Project":True}
dict2={"Name":"Sana","IsAvailable":True,}
dict["age"]=21
print(dict["Username"])
print(dict)
print(dict.items())
print(dict2.items())
print(dict.values())
print(dict.keys())
print(dict.update(dict2))
print(dict.popitem())
print(dict.pop("Project"))
#print(dict.clear())
print(dict.copy())
print(dict)

d={'a':1,'b':2,'c':3}
swap={j:k for k,j in d.items()}
print(swap)
print()
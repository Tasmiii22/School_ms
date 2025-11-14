set1={1,2,3}
set1.add(4)
set1.add(5)
set1.add(6)
print(set1)
set1.remove(2)
print(set1)
print(type(set1))
print(max(set1))
print(min(set1))
print(len(set1))
set1.add(8)
print(set1.update([11,12]))
print(set1)
copyset=set1.copy()
print(copyset)
set2={1,3,5,21,31,41,51}
print(set1 | set2)#union
print(set1.union(set2))#union
print(set1 & set2)#intersection
print(set1 - set2)#difference
print(set1^set2)#symmentric difference
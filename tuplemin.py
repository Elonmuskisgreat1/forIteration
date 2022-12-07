list1 = input("data: ").split(",")
#List can be created only this comphrehension.
for i in range(len(list1)):
    list1[i]= int(list1[i])
    
tup = tuple(list1)
print("min:",min(tup))

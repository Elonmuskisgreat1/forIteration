data = input("data: ")
list1 = data.split(",")

for i in range(len(list1)):
    list1[i]= int(list1[i])


tup = tuple(list1)

print("min:",min(tup))
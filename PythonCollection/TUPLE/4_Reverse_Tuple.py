input_tuple = (1,2,3,4,5,6)

list=[]

for x in reversed(input_tuple): #reversed the tuple and add into list
    list.append(x)

output = tuple(list) #type casting list into tuple

print(output)

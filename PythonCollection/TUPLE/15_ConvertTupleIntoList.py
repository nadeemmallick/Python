# convert tuple to a list and modified it the convert into tuple

t =(12,23,43)

temp_list = list(t) #change tuple into list

temp_list.append(50) #modified tuple
temp_list[1]=78

new_tuple =tuple(temp_list) #again convert modified list into tuple

print(new_tuple)
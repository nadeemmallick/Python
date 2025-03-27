num = [1,23,45,65,76,76]
newlist =[num for num in num if num<=65]
print(newlist)
newlist = num + newlist #add previous list in new list
print(newlist)
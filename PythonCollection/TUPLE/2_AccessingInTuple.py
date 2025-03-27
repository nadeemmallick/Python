colour =('red','blue','yellow','green','black')

#positive indexing, negative indexing, range indexing , negative range indexing
print(colour[2],colour[-1],colour[1:5])
print(colour[-2: ])

#checking colour is prestent or not
if  'green' in colour:
    print("green is present in tuple")
else:
    print("not presesent")

#concatenate tuple
more_colour = ("purple","orange")
colour1 = (colour+ more_colour)
print(colour1)

#unpacking tuple

colour0,co,te,ge,we = colour
print(colour0,co,te,ge,we)
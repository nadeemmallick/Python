name = {'nadeem','noman','don','jon'}

print(name,len(name),type(name))

#accessing items
for x in name :
    print(x)

#checkin name is present or not
if 'nadeem' in name:
    print("name is present")
else:
    print('not present in set')

#adding items in set
name.add('rahul')
print(name)

#add sequence in set
name_list={'bom','kom'}
name.update(name_list)
print(name)

#removing name from set
name.remove('nadeem')
print(name)


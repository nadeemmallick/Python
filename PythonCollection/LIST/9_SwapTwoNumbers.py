#given a list in python and provided the index the index of the element, write a program to swap two number

n = int(input('Enter the size of list :'))
list = []

for _ in range(n):
    num = int(input())
    list.append(num)

index1 = int(input("Enter index 1 :"))
index2 = int(input("Enter index 2 :"))
print(list)

temp = list[index1]
list[index1] = list[index2]
list[index2] = temp

print(list)



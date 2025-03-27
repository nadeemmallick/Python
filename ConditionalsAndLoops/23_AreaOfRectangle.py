length_of_rectangle = int(input("Enter the length of rectangle :"))
breath_of_rectangle = int(input("Enter the breath of rectangle :"))

area = length_of_rectangle * breath_of_rectangle
perameter = 2*(length_of_rectangle*breath_of_rectangle)

if length_of_rectangle*breath_of_rectangle>2*(length_of_rectangle*breath_of_rectangle):
    print("Area of rectangle is greater than perameter :",area)
else:
    print("Parameter is greater than area :",perameter)
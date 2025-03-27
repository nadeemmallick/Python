def outer_function(x): # outer function bhar se le ge
    print("value of x",x)
    
    def inner_function():
        y=int(input("enter the value of y",)) #inner function throug inner part of our program
        print("value of y",y)
        result = x+y
        return result
    
    return inner_function()

x=int(input("enter the value of x"))

output = outer_function(x)
print(output)
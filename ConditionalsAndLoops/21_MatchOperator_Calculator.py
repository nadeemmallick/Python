num1 = float(input("Enter the first number :"))
num2 = float(input("Enter the second number :"))

operator = input("Enter the operator")

match operator:
    case "+":
        print("sum is :",num1+num2)
    case "-":
        print("Difference is :",num1-num2)
    case "*":
        print("Product is :",num1*num2)
    case "/":
        print("Division is :",num1/num2)
    case _ :
        print("Enter valid operator ")


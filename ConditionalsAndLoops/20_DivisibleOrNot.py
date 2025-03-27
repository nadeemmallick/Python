num = int(input("Enter the number :"))

if num % 15 == 0:
    print("The number is divisible by 15")
else:

    if num % 3 == 0 or num % 5 ==0:
        print("Number is not divivided by 15 but it is dividisible by 5 or 3")
    else:
        print("Number is neither divided by 3 nor 5")
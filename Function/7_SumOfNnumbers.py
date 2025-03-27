def sumofN (n):
    sum = 0
    for i in range (1,n+1):
        sum+=i
    return sum
n =int (input("Enter the no:"))
output = sumofN (n)
print ("the sum of n is :",output)
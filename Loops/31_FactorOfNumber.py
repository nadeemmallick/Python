n = int(input("Enter the number :"))
f=1
for i in range(1,n+1):
    if n%i==0:
        f =i
        print(f)
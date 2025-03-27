cost_price = int(input("Enter the cost price of the product :"))
selling_price = int(input("Enter the selling price of product :"))

if cost_price > selling_price:
    print("shopkeeper face loss of :",cost_price-selling_price)

elif selling_price > cost_price:
    print("shopkeeper in profit of :",selling_price-cost_price)
    
else:
    print("Not made profit and loss")

  


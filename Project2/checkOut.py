
print ("Welcome to the checkout counter!  How many items are you purchasing today?")
Customeritems = int(input())
count= 0
shoppingItem = []
userPrice = []
userTotal = 0

while Customeritems != count:
	print ("Please enter the name of product  " +str(count + 1))
	shoppingItem.append(input())
	print ("And how much does " +str(shoppingItem[count]) + " cost?")
	userPrice.append(float(input()))
	userTotal = userTotal + userPrice[count]
	count = count + 1
	
print ("Your order was")
for i in range (len(shoppingItem)):
	print (shoppingItem[i] + " $" +str(userPrice[i]))
	
print ("Your subtotal comes to $" +str(userTotal) + ". With 9% sales tax, your total is " +str(userTotal *1.09) + ".")
	
print("Please enter cash amount:")
userPay = float(input())
userTotal = userPay - (userTotal*1.09)
print("I owe you back " +str(userTotal))
print("Thank you for shopping with us!")

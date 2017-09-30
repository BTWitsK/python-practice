# Allow a user to enter a quantity and price of an item. 
# Display the extended price (quantity x price). 
# If the quantity is greater than or equal to 1000, give a 10% discount.
# Otherwise when the quantity is less 1000 give a 1% discount.

#ask user for quantity and price of item
quantity = eval(input('How many items are you purchasing? '))

#ask user for the price per item
itemPrice = eval(input('What is the price of the item? '))

#Compute and display the extended price
price = quantity * itemPrice
print('The pretotal cost of the order is: ' + str(price))

if quantity > 1000:
    price = price * .90
    print('The total cost of the order is: ' + str(price)) 
else:
    price = price * .99
    print('The total cost of the order is: ' + str(price)) 

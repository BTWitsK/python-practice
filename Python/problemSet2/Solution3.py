# The program asks the user for a widget and quantity. 
# Determine the price of the widgets based on the chart below. 
# Display the price per widget, the total amount (extended price), the tax amount and the total order. 
# Widget A gets a 7% tax and B gets 10% tax.
 
#Widget			Price Per Widget
# A			$10.00
# B			$20.00

# Assume the widget has to be A or B. So if the Widget is not A then you can assume it is B.

widget = input('What widget are you purchasing? ')
widget = widget.upper()

qty = eval(input('How many are you purchasing? '))

if widget == 'A':
    price = 10
    tax = .07

else: 
    price = 20
    tax = .10

total = price * qty
tax *= total

print('The price per widget is ${}'.format(price))
print('The pretotal amount of your oder is ${}'.format(total))
print('The total tax amount is ${0:.2f}'.format(tax))
print('Your order total is ${0:.2f}'.format(total + tax))
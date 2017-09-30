#3. The price of an item and discount percent is entered
#into the program. Display the discount amount and
#discounted price of the item.

#get the price of the item and change it over to a float in case of decimals
price = eval(input('Enter the price of the item: '))

#get the discount percentage, convert it to a decimal and get the amount of the discount
discount = eval(input('Enter the % discount: '))
discount = price * (discount / 100)

#compute the price of the item after the discount is applied
discountPrice = price - discount

#displays the amount of the discount
print('The discount amount is: ${}'.format(discount))

#displays the price of the item after discount is applied
print('The discounted price of the item is: ${0:.2f}'.format(discountPrice))

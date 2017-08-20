# 2. Given the current stock price and quantity of stock, display the current value of the stock in your portfolio.

#Get the price and quantity from the user, then convert it to a string to properly display it
price = float(input('Enter the current price of the stock: '))
qty = float(input('How many shares do you own?: '))

#Compute total then convert it to a string to properly display it
total = str(price * qty)
print('The total value of your portfolio is: ' + total)

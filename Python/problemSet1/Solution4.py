#4. The purchase price and current price of a stock is entered into yourprogram.
#Display the percentage increase or decrease of the stock.

#gets the original purchase price from the user

purchasePrice = float(input('Enter the price of the stock when you bought it: '))

#gets the current price of the stock from the user

currentPrice = float(input('Enter the current price of the stock: '))

#computes the difference in price from the original purchase price to now

newPrice = purchasePrice - currentPrice

#computes the rate of change between the current price and the original price

percentageChange = newPrice / purchasePrice

if newPrice > 0:
    print('Your stock went down by '+(str(percentageChange * 100))+'%')
elif newPrice < 0:
    print('Your stock went up by ' + (str(percentageChange * -100))+'%')
else:
    print('Your stock has not changed')




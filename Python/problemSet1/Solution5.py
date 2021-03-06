#5. You are setting up a business and need to compute the break even point.
#This indicates how many items you must sell at a given price to cover your overhead.
#Enter fixed costs, price per unit and cost per unit into your program.
#Compute the break even point by dividing fixed costs by the difference of price per unit and cost per unit.

#Asks the user for the fixed cost of the item, and converts it to a float
fixedCost = eval(input('Enter fixed cost of the item: '))

#Asks the user for the price per unit of the item and converts it to a float
pricePerUnit = eval(input('Enter the price per unit of the item: '))

#Asks the user for the cost per unit of the item and converts it to a float
costPerUnit = eval(input('Enter the cost for each item: '))

#Computes the break even point by dividing fixed costs by the difference of price per unit and cost per unit.
breakEvenPoint = fixedCost/(pricePerUnit - costPerUnit)
print('The break even point is {}'.format(breakEvenPoint))


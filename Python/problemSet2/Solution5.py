#5. The warrantee of an appliance depends on the cost of the appliance. 
#For appliances over $1,000 the cost is 10% of the price. 
#For appliances $1,000 or less the cost is 5% of the price. 
#The user will enter the cost of an appliance. 
# Display the cost, the cost of the warrantee and the total.

cost = eval(input('What is the cost of the appliance? '))

if cost > 1000:
    warrantee = cost * .10
else:
    warrantee = cost *.05

print('The cost of the appliace is ${0:.2f}'.format(cost))
print('The cost of the warrantee is ${0:.2f}'.format(warrantee))
print('The total cost of purchase is ${0:.2f}'.format(cost + warrantee))

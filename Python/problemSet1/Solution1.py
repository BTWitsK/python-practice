#1. Get two numbers from the keyboard. Display the sum, product, difference and quotient of the two numbers.

#Gets the numbers from the user
firstNum = eval(input('Enter the first number: '))
secondNum = eval(input('Enter the second number: '))

#Remember input() takes whatever is typed as a string, float() changes this to a float to allow for decimals

#Compute the sum then change type to string to display
add = str(firstNum + secondNum)
print('The sum of your two numbers is: {}'.format(add))

#Does the same as the above code segment but for the product
product = str(firstNum * secondNum)
print('The product of your two numbers is: {}'.format(product))

difference = str(firstNum - secondNum)
print('The difference between your two numbers is: {}'.format(difference))

quotient = str(firstNum / secondNum)
print('The quotient of the two numbers is: {}'.format(quotient))

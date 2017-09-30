# Enter the number of books to order and cost per book. 
# If the cost of the order is over $50.00 do not charge tax. 
# If the order is $50.00 or under charge 7% sales tax. 
# Give the number ordered, amount of the book, the tax amount and the total due.

books = eval(input('How many books are you ordering? '))
cost = eval(input('What is the cost per book? '))

total = books * cost
tax = total * .07

#if the total amonut is less than $50 charge tax 
if total < 50:
    total += tax
else:
    pass



print('The number of books ordered is {}'.format(books))
print('The cost of each book is ${}'.format(cost))
print('The Cost of tax for the books is ${0:.2f}'.format(tax))
print('The total amount of your oder is ${0:.2f}'.format(total))

#Given a student’s last name and GPA, display the last name, GPA
#and a message of “Well Done” when the GPA is greater than or equal to 4.0.
#When the GPA is less than 4.0 display a message “Good Effort”. 

name = input('What is your name? ')
GPA = eval(input('What is your GPA? '))

if GPA >= 4.0:
    message = 'Well Done'
else:
    message = 'Good Effort'

print('{}, your GPA is {}: {}'.format(name,GPA,message))
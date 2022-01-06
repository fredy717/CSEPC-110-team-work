def favoriteColor():
    name=input('what is your name: ')
    lastName=input('what is your last name: ')
    color=input('Please type your favorite color: ')
    return 'Hi! \nYou are %s %s and your favorite color is: "%s".' % (name.capitalize(), lastName.capitalize(),color)

print(favoriteColor())
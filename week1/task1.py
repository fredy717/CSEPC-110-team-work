def favorite_color():
    first_name = input('what is your name: ')
    last_name = input('what is your last name: ')
    color = input('Please type your favorite color: ')
    return 'Hi! \nYou are %s %s and your favorite color is: "%s".' \
           % (first_name.capitalize(), last_name.capitalize(), color)


print(favorite_color())

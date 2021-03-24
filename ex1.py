print('Hello World!')
print('Hello Again')
print('I llike this typing')
print('This is fun')
print('Yay! Printing')
print("I'd much rather you 'not'.")
print('I "said" do not touch this')
print(100 - 25*3%4)

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print('There are', cars, 'cars available')
print('There are only', drivers, 'drivers available')
print('There will be', cars_not_driven, 'empty cars today')
print('We can transport', carpool_capacity, 'people today')
print('We have', passengers, 'passengers to carpool today')
print('We need to put about', average_passengers_per_car, 'in each car')

_name = 'Donkey A.Real One'
_age = 30#years
_height = 77#inches
_weight = 180#pounds
_eyes = 'Turchoise'
_teeth = 'White'
_hair = 'Grey'

print(f"Let's talk about '{_name}'.")
print(f"He's {_height} inches tall.")
print(f"He's {_weight} pounds heavy.")
print(f"Actually that is too heavy.")
print(f"He's got {_eyes} eyes and {_hair} hair.")
print(f'His teeth are usually {_teeth} depending on the coffee.')
#This line is tricky, try to get it exactly right
total = _age+ _height + _weight
print(f"If I add {_age}, {_height}, and {_weight} I get {total}.")

types_of_people = 10
x = f"There are {types_of_people} types of people."
binary  = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."
print(x)
print(y)
print(f"I said: {x}")
print(f"I also said: {y}")
hilarious = False
joke_evaluation = "Isn't that joke so funny?!{}"
print(joke_evaluation.format(hilarious))
w = "This is the left side of..."
e = "a string with a right side"
print(w + e)

print('****************************')
print('\n\n')
print('Mary had a little lamb.')
print("It's fleece was as white as {}.".format('snow'))
print('And everywhere Mary went.')
print('.'*10)#what'd that do?

end1 = "C"
end2 = "h"
end3 = 'e'
end4 = 'e'
end5 = 's'
end6 = 'e'
end7 = 'B'
end8 = 'u'
end9 = 'r'
end10 = 'g'
end11 = 'e'
end12 = 'r'

#Watch that comma at the end. Remove it and see what happens
print(end1 + end2 + end3 + end4 + end5 + end6, end = ' ')
print(end7 + end8 + end9 + end10 + end11 + end12)

print('****************************')
print('\n\n')
formatter = "{} {} {} {}"
print(formatter.format(1,2,3,4))
print(formatter.format('one','two','three','four'))
print(formatter.format(True,False,False,True))
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format("Try your","Own text here", "May be a poem", "Or a song about fear"))
print('\n****************************\n\n')

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec"
print('Here are the days:',days)
print('Here are the months:', months)
print("""There's something going on here.
With the three doublw-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")
print('\n****************************\n\n')
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
\a
"""
single_cat = ''' Hi Im single
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print(single_cat)

print('\n****************************\n\n')
"""
print('How old are you?', end = ' ')
age = input()
print('How tall are you?', end = ' ')
height = input()
print('How much do you weigh?', end = ' ')
weight = input()
print(f'So, you\'re {age} years old, {height} inches tall, and {weight} pounds heavy.')

print('\n****************************\n\n')

age = input('How old are you? ')
height = input('How tall are you? ')
weight = input('How much do you weigh? ')
print(f'So, you\'re {age} years old, {height} inches tall, and {weight} pounds heavy.')

print('\n****************************\n\n')
from sys import argv

scr, first, second, third = argv
print("The script you called:", scr)
print("The first arg you passed:", first)
print("The second arg you passed:", second)
print("The third arg you passed:", third)

print('\n****************************\n\n')

from sys import argv
script, user_name = argv
prompt = '> '
print(f"Hi {user_name}, I'm the {script} script.")
print(f"I'd like to ask you a few questions.")
print(f"Do you like me, {user_name}?")
likes = input(prompt)
print(f"Where do you live {user_name}?")
lives = input(prompt)
print(f"What kind of computer do you have?")
computer = input(prompt)
print(f'''Allright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer.
Nice.''')

print('\n****************************\n\n')
"""

from sys import argv

script, file_name = argv
txt = open(file_name)
print(f"Here's your file: {file_name}")
print(txt.read())

print("Type the file name again:")
file_again = input('> ')
txt_again = open(file_again)
print(txt_again.read())

print('\n****************************\n\n')


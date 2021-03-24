# loops and lists

the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# first kind of for loop

for number in the_count:
    print(f"This is count {number}")

# same as above

for fruit in fruits:
    print(f"A fruit of type {fruit}")

# we can go through mixed loops too

for i in change:
    print(f"I got {i}")

# we can also build lists
# start with empty

elements = []

# then use a range funtion 
for i in range(1, 6):
    print(f"Adding {i} to the list")
    elements.append(i)

for i in elements:
    print(f"Element was {i}")


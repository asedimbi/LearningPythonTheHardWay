#While loops

i = 0
numbers = []

while i<6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i+1
    print("Numbers are now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)

def looper(start, end, inc):
    return list(range(start, end, inc))

print(looper(5,15,2))


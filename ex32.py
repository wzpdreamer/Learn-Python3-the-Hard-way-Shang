count = [1, 2, 3, 4, 5]
fruits = ['apples', 'orange', 'pears', 'apricots']
change = ['pennies', 'dimes', 'quarters']
for number in count:
    print(f"This is count {number}")
for fruit in fruits:
    print(f"A fruit of type: {fruit}")
for i in change:
    print(f"I got {i}")
elements = []
for i in range(0,8):
    print(f"Adding {i} to the list.")
    elements.append(i)
for i in elements:
    print(f"Element was {i}")
i=0;
numbers = []
while i < 8:
    print(f"At the top i is {i}")
    numbers.append(i)
    i = i + 1
    print("Numbers now:",numbers)
    print(f"At the botton i is {i}")
print("The numbers: ")
j=0
while j<i:
    j=j+1
    print(numbers[j])

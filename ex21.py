def add(a,b):
    print(f"ADDING {a} + {b}")
    return  a + b
def subtract(a,b):
    print(f"SUBTRACTING {a} - {b}")
    return  a - b
def multiply(a,b):
    print(f"MULTIPLYING {a} * {b}")
    return  a * b
def divide(a,b):
    print(f"DIVIDING {a} / {b}")
    return  a / b
print("Let's do some math with just functions!")
age = add(30,31)
height = subtract(62,1)
weight = multiply(50,2)
iq = divide(100,2)
print(f"Age: {age},Height: {height},Weight: {weight},IQ:{iq}")
print("Here is a puzzle.")
what = add(age, subtract(height, multiply(weight, divide(iq,5))))
print("That becomes: ", what, "Can you do it by hand?")
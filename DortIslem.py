def add (a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


age = add(30, 5)
height = subtract(178, 4)
weight = multiply(40, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" %(age, height, weight, iq)

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print "That becomes: ", what, " Can you do it by hand?"

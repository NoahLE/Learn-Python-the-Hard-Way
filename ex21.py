def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b


def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b


def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b


def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

# working from inner to outer nested functions
# add(age, subtract(height, multiply(weight, divide(iq, 2))))
# add(age, subtract(height, multiply(weight, divide(50, 2))))
# add(age, subtract(height, multiply(weight, 25)))
# add(age, subtract(height, multiply(180, 25)))
# add(age, subtract(height, 4500))
# add(age, subtract(74, 4500))
# add(age, -4426)
# add(35, -4426)
# -4391
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

# Study drills
# 2. what = (age+(height-(weight*(iq/2))))
# 4. what_what = ((age * iq) + (weight * iq)) - height
#    what_what = subtract(add(multiply(age, iq), multiply(weight, iq)))
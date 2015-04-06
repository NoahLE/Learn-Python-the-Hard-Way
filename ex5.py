name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)

# Study drills
# 1. find and replace is your friend :P
# 2. cm = in / 0.3936
#    kg = lb / 2.2046
metric_weight = weight / 2.2046
metric_height = height / 0.3936
print "In metric units, %s is %d kilograms and %d centimeters" % (name, metric_weight, metric_height)
# 3. https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting
# 4. https://docs.python.org/2/library/string.html#format-examples
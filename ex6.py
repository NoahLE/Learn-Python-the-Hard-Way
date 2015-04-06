# declares and assigns values to variables
# study drill 2
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# study drill 2
y = "Those who know %s and those who %s." % (binary, do_not)

# prints various variables
print x
print y

# study drill x2
print "I said: %r." % x
print "I also said: '%s'." % y

# more variable assignment
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# printing (note the %r in joke_evaluation)
# study drill 2
print joke_evaluation % hilarious

# string concatenation
w = "This is the left side of..."
e = "a string with a right side."

# concatenates the variables w and e to make the sentence in the output
print w + e
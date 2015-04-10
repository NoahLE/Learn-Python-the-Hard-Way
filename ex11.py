print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

# study drills
# 1. http://www.cyberciti.biz/faq/python-raw_input-examples/
# 2.
noodle = raw_input("What is a type of pasta? \n>>>")
print "You typed: {0}".format(noodle)
# 3.
question = input("What was the name of Sir Francis Drake's ship?: ")
print "What's {0}".format(question)
# 4. I assume this happens because raw input strings are stored in single quotes
# http://stackoverflow.com/a/647787
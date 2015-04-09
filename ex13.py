from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# Study drills
# 1.
# $ python ex13.py arg1 arg2
# Traceback (most recent call last):
#   File "ex13.py", line 3, in <module>
#     script, first, second, third = argv
# ValueError: need more than 3 values to unpack
#
# The error message is weirdly worded in my opinion, but you can see that it needs more values.
# Another hint is looking at line 3 of ex13.py will give you an idea that it has to do something with the variables

# 2.
# script, transifex = argv
# print "What's the coolest localization company ever? ", transifex

# the loop below is just a sample, don't worry about it too much
# script, var1, var2, var3, var4 = argv
# print "Here's some random words: "
# for argument in argv:
#     print argument

# 3.
# print "Welcome to this lame interactive prompt."
# script, fname = argv
# print "Hi {0}.".format(fname) + " Could you answer these for science?"
# favorite_cake = raw_input("What's your favorite cake? ")
# pie_cake = raw_input("Do you like cake or pie more? ")
# print "{0}, is a cool person who likes {1} and thinks {2} is the best.".format(fname, favorite_cake, pie_cake)
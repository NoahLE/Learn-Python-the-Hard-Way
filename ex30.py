people = 30
cars = 20
trucks = 15

# If there are more cars than people, take them. If there are fewers cars than people, don't take them.
# If cars and people are equal, we can't decide.
if cars > people and cars > trucks and trucks < people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

# If trucks or cars are greater than the other, then there are too many. Otherwise, we can't decide.
if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

# if there are more people than trucks, print the first statement
if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."

# Study drills
# 1. If the first if statement fails, try the elif statement. If the elif statement
#    fails or does not exist, execute the else statement
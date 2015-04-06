animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']


def print_animal(location):
    if location == 0:
        tense = 'st'
    elif location == 1:
        tense = 'nd'
    elif location == 2:
        tense = 'rd'
    else:
        tense = 'th'

    print 'The {0}{1} animal is at {2} and is a {3}.'.format(location + 1, tense, location, animals[location])
    print 'The animal at {0} is the {1}{2} animal and is a {3}.'.format(location, location + 1, tense, animals[location])
    print '--==--'

# The animal at 1.
print_animal(1)
# The third (3rd) animal.
print_animal(2)
# The first (1st) animal.
print_animal(0)
# The animal at 3.
print_animal(3)
# The fifth (5th) animal.
print_animal(4)
# The animal at 2.
print_animal(2)
# The sixth (6th) animal.
print_animal(5)
# The animal at 4.
print_animal(4)

# Study drills
# 1. Years are ordinal, not cardinal
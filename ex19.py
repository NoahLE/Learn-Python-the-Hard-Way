# creates the cheese_and_crackers function and accepts two variables
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # prints each of the variables and strings listed below
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
# calling the cheese_and_crackers function with integers
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
# assigns the numbers to the variables listed on the left
amount_of_cheese = 10
amount_of_crackers = 50

# calls the cheese_and_crackers with while passing the variables declared above
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
# does arithmetic addition before calling the function
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
# adds numbers to the variables declared above and calls the cheese_and_crackers function
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


# study drills
# wrote 7 alternative print methods
def printing_some_stuff(dog_name, dog_breed, weight, height, color):
    print 'Patient name: {0}'.format(dog_name)
    print '-=-\nColor: {0}\nDog breed: {1}\nWeight: {2}\nHeight: {3}'.format(color, dog_breed, weight, height, color)


def printing_some_stuff_2(dog_name, dog_breed, weight, height, color):
    print 'Patient name: {0}'.format(dog_name)
    print '-=-\nColor: %s\nDog breed: %s\nWeight: %s\nHeight: %s' % (color, dog_breed, weight, height, color)

# printing_some_stuff('sparky', 'hound', '50 lbs', '3 ft', 'brown')
# printing_some_stuff_2('sparky', 'hound', '50 lbs', '3 ft', 'brown')

name = 'sparky'
breed = 'hound'
weight = '50 lbs'
height = '3 ft'
color = 'brown'

# printing_some_stuff(name, breed, weight, height, color)


def call_printing_function():
    printing_some_stuff(name, breed, weight, height, color)

# call_printing_function()


def getting_input():
    dog_name = raw_input("What's your dog's name?\n>>> ")
    print('woof', dog_name)

# getting_input()


def write_to_file(name, breed, weight, height, color):
    text_19 = open('ex19.txt', 'w+')
    text_19.write(name + ', ' + breed + ', ' + weight + ', ' + height + ', ' + color)
    text_19.close()
# write_to_file(name, breed, weight, height, color)


def read_dog():
    text_19 = open('ex19.txt', 'r')
    file_contents = text_19.read()
    print(file_contents)
    text_19.close()

# read_dog()


def read_dog_2():
    text_19 = open('ex19.txt', 'r')
    file_contents = text_19.read()
    file_contents = file_contents.split(', ')
    for item in file_contents:
        print item
    text_19.close()

# read_dog_2()
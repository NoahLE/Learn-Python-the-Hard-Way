# import argv function from sys library
from sys import argv

# unpacks arguments provided by user
script, input_file = argv


# prints object f
def print_all(f):
    print f.read()


# resets to beginning of file
def rewind(f):
    f.seek(0)


# prints the line count (integer) and line
def print_a_line(line_count, f):
    print line_count, f.readline()

# opens file
current_file = open(input_file)

print "First let's print the whole file:\n"

# prints contents of file
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# resets pointer to beginning of file
rewind(current_file)

print "Let's print three lines:"

# goes through file, line by line, and prints contents
# prints first line in file
current_line = 1
print_a_line(current_line, current_file)

# you can add values to variables this way
# prints second line in file
current_line = current_line + 1
print_a_line(current_line, current_file)

# or like this
# prints third line in file
current_line += 1
print_a_line(current_line, current_file)

# Study drills
# 4. https://docs.python.org/2/tutorial/inputoutput.html
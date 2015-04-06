# imports the argument function from the sys library
from sys import argv

# assigns the input to variables
script, filename = argv

# opens the text file
txt = open(filename)

# prints the filename and the file contents
print "Here's your file %r:" % filename
print txt.read()
txt.close()

# reprompts for file name and accepts input via the terminal
print "Type the filename again:"
file_again = raw_input("> ")

# opens the file
txt_again = open(file_again)

# prints the contents of the file
print txt_again.read()
txt_again.close()

# Study drill
# 5. It depends on the project setup but having a variable via argument seems like it would
#    be faster since it doesn't stop the program for the user's input. The variable in the program
#    on the other than makes the program more modular since just using arguments would involve
#    rewriting the initial input.
#
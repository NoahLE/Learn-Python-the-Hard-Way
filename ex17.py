from sys import argv
from os.path import exists

script, from_file, to_file = argv

file_data = (open(from_file, 'r')).read()

print "Copying from {0} to {1}. \nIt is {2} bytes. \nIt exists: {3}".format(from_file, to_file,
                                                                            len(file_data), exists(to_file))

out_file = open(to_file, 'w+').write(file_data)

print "Done."

# Study drills
# 1. A good way to think about this is if a = b + 1 and x = a + 2, then x = b + 1 + 2
# 2. This is the shortest I could get mine without using semicolons to break things up.
#    This could also be done in one line by doing 'cat ex16.txt > ex17.txt'
# 3. Use q to quit. Arrow keys or hjkl to navigate.
# 4. https://mail.python.org/pipermail/tutor/2012-January/088031.html
# 5. https://docs.python.org/3/reference/import.html

# from sys import argv
# from os.path import exists
#
# script, from_file, to_file = argv
#
# file_data = (open(from_file, 'r')).read()
#
# print "Copying from {0} to {1}. \nIt is {2} bytes. \nIt exists: {3}".format(from_file, to_file,
#                                                                             len(file_data), exists(to_file))
#
# out_file = open(to_file, 'w+').write(file_data)
#
# print "Done."


# from sys import argv
# from os.path import exists
#
# script, from_file, to_file = argv
#
# print "Copying from %s to %s" % (from_file, to_file)
#
# # we could do these two on one line, how?
# in_file = open(from_file)
# indata = in_file.read()
#
# print "The input file is %d bytes long" % len(indata)
#
# print "Does the output file exist? %r" % exists(to_file)
# print "Ready, hit RETURN to continue, CTRL-C to abort."
# raw_input()
#
# out_file = open(to_file, 'w')
# out_file.write(indata)
#
# print "Alright, all done."
#
# out_file.close()
# in_file.close()